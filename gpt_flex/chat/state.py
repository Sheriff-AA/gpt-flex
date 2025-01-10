from typing import List
import asyncio
import reflex as rx

from gpt_flex.models import ChatSession, ChatSessionMessageModel
from . import ai

class ChatMessage(rx.Base):
    message: str
    is_bot: bool = False


class ChatState(rx.State):
    chat_session: ChatSession = None
    did_submit: bool = False
    messages: List[ChatMessage] = []

    @rx.var
    def user_did_submit(self) -> bool:
        return self.did_submit
    
    def create_new_chat_session(self):
        with rx.session() as db_session:
            obj = ChatSession()
            db_session.add(obj)
            db_session.commit()
            db_session.refresh(obj)
            self.chat_session = obj

    def clear_and_start_new(self):
        self.chat_session = None
        self.create_new_chat_session()
        self.messages = []
        yield
    
    def on_load(self):
        if self.chat_session is None:
            self.create_new_chat_session()

    def insert_message_to_db(self, content, role='unknown'):
        if self.chat_session is None:
            return 
        
        if not isinstance(self.chat_session, ChatSession):
            return
        with rx.session() as db_session:
            data = {
                "session_id": self.chat_session.id,
                'content': content,
                "role": role
            }
            obj = ChatSessionMessageModel(**data)
            db_session.add(obj)
            db_session.commit()
        
    def append_message_to_ui(self, message, is_bot: bool=False):
        if self.chat_session is not None:
            print(self.chat_session.id)
        self.messages.append(
                ChatMessage(
                    message=message,
                    is_bot=is_bot,
                )
            )

    async def handle_submit(self, form_data: dict):
        print(form_data)
        user_message = form_data.get('message')
        if user_message:
            self.did_submit = True
            self.append_message_to_ui(user_message, False)
            self.insert_message_to_db(user_message, role='user')
            yield
            gpt_messages = self.get_gpt_messages()
            bot_response = ai.get_llm_response(gpt_messages)
            # await asyncio.sleep(2)
            self.did_submit = False
            self.append_message_to_ui(bot_response, True)
            self.insert_message_to_db(bot_response, role='system')

            yield

    def get_gpt_messages(self):
        gpt_messages = [
            {
                "role": "system",
                "content": "You are an expert at creating recipies like an elite chef. Respond in markdown"
            }
        ]
        for chat_message in self.messages:
            role = 'user'
            if chat_message.is_bot:
                role = 'system'
            gpt_messages.append({
                'role': role,
                'content': chat_message.message
            })

        return gpt_messages
