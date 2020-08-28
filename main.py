from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from screenhelper import *
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.list import TwoLineListItem
from database import db

Builder.load_string(
    s
)


class ContentNavigationDrawer(BoxLayout):
    pass


class CustomOneLineIconListItem(TwoLineListItem):
    pass


class CustomIconButtonItem(MDRectangleFlatIconButton):
    pass


class PreviousMDItems(Screen):

    def set_list_md_items(self, text="", search=False):

        def add_item(text):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "text": text[0],
                    "secondary_text": text[1],
                    "callback": lambda x: x,
                }
            )

        self.ids.rv.data = []
        for i in range(1, len(db["Strings"])):
            if search:
                if text.lower() in db["Strings"][i][0].lower():
                    add_item(db["Strings"][i])
            else:
                add_item(db["Strings"][i])

    def set_list_button_items(self, text="", search2=False):

        def add_item(category):
            self.ids.rv2.data.append(
                {
                    "viewclass": "CustomIconButtonItem",
                    "icon": db[category][0],
                    "text": category,
                    "callback": lambda x: x,
                }
            )

        self.ids.rv2.data = []
        for category in db.keys():
            if search2:
                print(text + "1")
                if text.lower() in category.lower():
                    add_item(category)
            else:
                print(category)
                add_item(category)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = PreviousMDItems()

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"
        return self.screen

    def on_start(self):
        self.screen.set_list_md_items()
        self.screen.set_list_button_items()


MainApp().run()
