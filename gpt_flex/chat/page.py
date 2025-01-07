import reflex as rx

from gpt_flex import ui



def chat_page() -> rx.Component:

    return ui.base_layout(
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )

