from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from screenhelper import *
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatIconButton
from database import db
from kivymd.uix.label import MDLabel

Builder.load_string(
    s
)


class ContentNavigationDrawer(BoxLayout):
    pass


class CustomItem(MDLabel):
    pass


class CustomIconButtonItem(MDRectangleFlatIconButton):
    pass


class PreviousMDItems(Screen):

    def set_list_md_items(self, text="", search=False, category="Basics"):

        def add_item(text):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomItem",
                    "text": "----" * 30 + "\n" + text[0] + "\n" * 2 + text[1],
                    "callback": lambda x: x,
                }
            )

        self.ids.rv.data = []
        for i in range(1, len(db[category])):
            if search:
                if text.lower() in (db[category][i][0].lower()) or text.lower() in (db[category][i][1].lower()):
                    add_item(db[category][i])
            else:
                add_item(db[category][i])

    def set_list_button_items(self, text="", search2=False):

        def add_item(category):
            self.ids.rv2.data.append(
                {
                    "viewclass": "CustomIconButtonItem",
                    "icon": db[category][0],
                    "text": category,
                    "callback": lambda x: x,
                    "on_press": lambda x=category: self.set_list_md_items("", True, category),

                }
            )

        self.ids.rv2.data = []
        for category in db.keys():
            if search2:
                if text.lower() in category.lower():
                    add_item(category)
            else:
                add_item(category)



class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = PreviousMDItems()

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "700"
        return self.screen

    def on_start(self):
        self.screen.set_list_md_items()
        self.screen.set_list_button_items()


MainApp().run()
