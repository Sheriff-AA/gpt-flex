import reflex as rx

from .state import ChatState

def chat_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.text_area(
                name='message',
                placeholder='Enter your message here',
                required=True,
                width='100%',
            ),
            rx.button('Submit', type='submit'),
        ),
        on_submit=ChatState.handle_submit,
        reset_on_submit=False,
    )

