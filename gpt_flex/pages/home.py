import reflex as rx
from rxconfig import config

from gpt_flex import ui

def home_page() -> rx.Component:
    # Welcome Page (Index)
    return ui.base_layout(
        # rx.color_mode.button(position="bottom-left"),
        rx.vstack(
            rx.heading("Welcome to THE PLAYGROUND!", size="9"),
            rx.text(
                "LET'S PLAY!",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )