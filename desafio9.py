from kivy.app import App
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        return Label(text='Kivy App Corrigido')

MinhaApp().run()