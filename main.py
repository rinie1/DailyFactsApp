from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class DailyFactsApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, DailyFacts", halign="center")


DailyFactsApp().run()