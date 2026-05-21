from textual.app import App
from textual.widgets import Header, Footer, ScrollView, Input

class TermChat(App):

    def __init__(self):
        super().__init__()
     
    def compose(self):
        yield Header()
        self.body = ScrollView()
        yield self.body
        self.input = Input(placeholder="Type your message here...")
        yield self.input
        yield Footer()

    async def on_input_submitted(self, message):
        user_message = message.value
        # Here you would typically send the user_message to your backend or chatbot logic
        response = f"Echo: {user_message}"  # Placeholder response
        await self.body.update(response)
        self.input.value = ""  # Clear the input after submission