"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to km
"""
from importlib.metadata import pass_none

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_COEFFICIENT = 1.61


class ConvertMilesKm(App):
    """ Kivy app to convert miles to km """
    output_message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Miles to Km Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        try:
            miles = float(self.root.ids.mile_text_input.text)
            km = MILES_TO_KM_COEFFICIENT * miles
            self.output_message = f"{km:.2f}"
        except ValueError:
            self.output_message = "0.0"

    def handle_increment_button(self, increment):
        try:
            miles = float(self.root.ids.mile_text_input.text)
            miles += increment
            self.root.ids.mile_text_input.text = str(miles)
        except ValueError:
            miles = increment
            self.root.ids.mile_text_input.text = str(miles)


ConvertMilesKm().run()
