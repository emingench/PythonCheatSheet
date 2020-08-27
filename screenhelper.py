
screen_search = '''


<CustomOneLineIconListItem>:

    IconLeftWidget:
        icon: root.icon


<PreviousMDItems>:

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)

        BoxLayout:
            size_hint_y: None
            height: self.minimum_height

            MDIconButton:
                icon: 'magnify'

            MDTextField:
                id: search_field
                hint_text: 'Search'
                on_text: root.set_list_md_items(self.text, True)

        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'

            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
'''
s = '''
<CustomOneLineIconListItem>:


<PreviousMDItems>:

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(50)

        

        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'

            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
        
           

    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'
                    canvas:
                        Color:
                            rgba: .2,.2,.2,1

                    MDToolbar:
                        title: "Python Cheat Sheet"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                          
                        
                    Widget:
                    BoxLayout:
                        size_hint_y: None
                        height: self.minimum_height
            
                        MDIconButton:
                            icon: 'magnify'
            
                        MDTextField:
                            id: search_field
                            hint_text: 'Search'
                            on_text: root.set_list_md_items(self.text, True)  
                    


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                BoxLayout:
                    orientation: 'vertical'
                    spacing: dp(10)
                    padding: dp(20)
                    
                    BoxLayout:
                        size_hint_y: None
                        height: self.minimum_height
            
                        MDIconButton:
                            icon: 'magnify'
            
                        MDTextField:
                            id: search_field2
                            hint_text: 'Search'
                            on_text: root.set_list_md_items(self.text, True)
                    RecycleView:
                        id: rv2
                        key_viewclass: 'viewclass'
                        key_size: 'height'

                    RecycleBoxLayout:
                        padding: dp(10)
                        default_size: None, dp(48)
                        default_size_hint: 1, None
                        size_hint_y: None
                        height: self.minimum_height
                        orientation: 'vertical'
            '''