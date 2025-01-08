from typing import List
import asyncio
import reflex as rx

from gpt_flex.models import Chat
from . import ai

class ChatMessage(rx.Base):
    message: str
    is_bot: bool = False


class ChatState(rx.State):
    did_submit: bool = False
    messages: List[ChatMessage] = []

    @rx.var
    def user_did_submit(self) -> bool:
        return self.did_submit
    
    def on_load(self):
        with rx.session() as session:
            results = session.exec(Chat.select()).all()
            print(results)

    
    def append_message(self, message, is_bot: bool=False):
        return self.messages.append(
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
            self.append_message(user_message, False)
            yield
            gpt_messages = self.get_gpt_messages()
            bot_response = ai.get_llm_response(gpt_messages)
            # await asyncio.sleep(2)
            self.did_submit = False
            self.append_message(bot_response, True)
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
