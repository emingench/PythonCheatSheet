
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
        
        height: self.minimum_height
        BoxLayout:
            spacing: dp(10)
            padding: dp(40)
            size_hint_y: None
            height: self.minimum_height   

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
        BoxLayout:
            spacing: dp(10)
            padding: dp(25)
            size_hint_y: None
            height: self.minimum_height 
        
           

    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'
                    
                     

                    MDToolbar:
                        title: "Python Cheat Sheet"
                        elevation: 11
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                        BoxLayout:
                            size_hint_y: None
                            height: self.minimum_height
                
                
                            MDTextField:
                                id: search_field2
                                hint_text: 'Search'
                                color_mode: 'custom'
                                on_text: root.set_list_md_items(self.text, True)
                                line_color_focus: 1, 1, 1, 1
                            
                            MDIconButton:
                                icon: 'magnify'
                                theme_text_color: "Custom"
                                text_color: 1,1,1,1
                          
                        
                    Widget:
                      


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                Screen:
            '''