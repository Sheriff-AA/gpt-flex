import reflex as rx

from . import routes


class NavState(rx.State):
    def to_home(self):
        """
        Navigate to home page
        """
        return rx.redirect(routes.HOME_ROUTE)
    
    def to_about_us(self):
        """
        Navigate to about page
        """
        return rx.redirect(routes.ABOUT_ROUTE)
    
    def to_chat_page(self):
        """
        Navigate to chat page
        """
        return rx.redirect(routes.CHAT_ROUTE)