"""
CP1404/CP5632 Practical
Kivy GUI program to greet user
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """ Kivy app to get user's name and greet them """

    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Print greeting message to output label"""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear the output label"""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
