from textual.app import App
from textual.widgets import Header, Footer, ScrollView, Input

class TermChat(App):

    def __init__(self):
        super().__init__()
        
    async def on_mount(self):
        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")
        self.body = ScrollView()
        await self.view.dock(self.body, edge="left")
        self.input = Input(placeholder="Type your message here...")
        await self.view.dock(self.input, edge="bottom")

    async def on_input_submitted(self, message):
        user_message = message.value
        # Here you would typically send the user_message to your backend or chatbot logic
        response = f"Echo: {user_message}"  # Placeholder response
        await self.body.update(response)
        self.input.value = ""  # Clear the input after submission