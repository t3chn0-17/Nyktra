from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Button

class Nyktra(App):
  TITLE = "NYKTRA Server Dashboard"

  # BINDINGS = [("t", "toggle_dark", "Toggle dark mode")]

  def compose(self) -> ComposeResult:
    yield Header()
    yield Footer()


app = Nyktra()