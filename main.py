from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from screenhelper import *
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem


Builder.load_string(
    s
)

class ContentNavigationDrawer(BoxLayout):
    pass

class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class PreviousMDItems(Screen):

    def set_list_md_items(self, text="", search=False):

        def add_item(text):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "icon": 'language-python',
                    "text": text,
                    "callback": lambda x: x,
                }
            )

        self.ids.rv.data = []
        for i in ['a','b','c']:
            if search:
                if text in i:
                    add_item(i)
            else:
                add_item(i)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = PreviousMDItems()

    def build(self):
        return self.screen

    def on_start(self):
        self.screen.set_list_md_items()


MainApp().run()