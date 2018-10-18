import os
os.environ['KIVY_TEXT'] = "pango"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class PangoApp(App):
    def build(self):
        bl = BoxLayout(orientation="vertical")

        text_input = TextInput(font_context="system://")
        button = Button(text="تست", font_context="system://")
        label = Label(text="تست", font_context="system://")

        bl.add_widget(text_input)
        bl.add_widget(button)
        bl.add_widget(label)

        return bl


if __name__ == "__main__":
    PangoApp().run()
