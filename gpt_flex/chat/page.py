import reflex as rx

from gpt_flex import ui

from .form import chat_form

def chat_page() -> rx.Component:

    return ui.base_layout(
        rx.vstack(
            rx.heading("CHAT PAGE", size="9"),
            chat_form(),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )

