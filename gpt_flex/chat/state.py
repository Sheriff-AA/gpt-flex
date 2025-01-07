import reflex as rx


class ChatState(rx.State):
    def handle_submit(self, form_data: dict):
        print(form_data)

