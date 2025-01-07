"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from . import pages, navigation, chat

class State(rx.State):
    """The app state."""

    ...


app = rx.App()
app.add_page(pages.home_page, route=navigation.routes.HOME_ROUTE)
app.add_page(pages.about_us_page, route=navigation.routes.ABOUT_ROUTE)
app.add_page(chat.chat_page, route=navigation.routes.CHAT_ROUTE)

