"""
CP1404/CP5632 Practical
Kivy GUI program to dynamically create labels
"""
import random

from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabels(App):
    """ Kivy app to display a list of names """

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.names = ["Kit", "Hannah", "Toby", "Ebony", "Ethan", "Sebby"]

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Name List"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            # create a button for each data entry, specifying the text
            temp_label = Label(text=name)
            colour = tuple(random.random() for i in range(3)) + (1,)  # Extra extension to randomly assign colour
            temp_label.color = colour
            # add the button to the "main_box" layout widget
            self.root.ids.main_box.add_widget(temp_label)


DynamicLabels().run()
