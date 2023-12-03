from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from styles import Styles
from kivy.uix.boxlayout import BoxLayout

Builder.load_string("""
<CButton>:
    background_color: self.bg_color
    background_normal: ''
    on_press: root.pressed()
    on_release: root.released()
                    
<EdButton>:
    background_color: self.bg_color
    background_normal: ''
                    
<CTextInput>:
    padding: dp(15)
    background_normal: ''
    background_color: self.bg_color                        
    font_name: 'robotolight.ttf'
    font_size: '16sp'
                    
<SignupText>:
    color: self.bg_color
                    
<MButton>:
    background_color: self.menu_color
    background_normal: ''
    border: (25, 25, 25, 25)
    on_press: root.pressed()
    on_release: root.released()
    font_size: dp(30)
    font_name: 'robotomedium.ttf'
                    
<QButton>:
    background_color: self.menu_color
    background_normal: ''
    on_press: root.pressed()
    on_release: root.released()
    font_size: dp(30)
    font_name: 'robotomedium.ttf'
    size_hint: (None, None)
    size: (432, 40)
    halign: 'center'
    valign: 'center'            
                    

<MenuPalavra>:
    BoxLayout:
        size_hint_y: 0.125
        orientation: 'horizontal'
        canvas.before:
            Color:
                rgba: root.word_color
            RoundedRectangle:
                pos: (self.pos[0]+dp(12), self.pos[1])
                size: (self.size[0]*0.95, self.size[1]*0.90)
        BoxLayout:
            size_hint_x: 0.50
            Label:
                id: p7
                text: 'abandoned'
                halign: 'left'
                font_name: 'robotomedium.ttf'
                text_size: self.width, None
                size: self.texture_size
                font_size: '36sp'
        Button:
            size_hint: 0.15, 0.95
            id: s7
            background_normal: 'star.png'    
            #on_press: root.linkProfileAndWord(7)  
        Button:
            size_hint: 0.15, 0.95
            id: star
            size: self.size
            background_normal: 'next.png'
            #on_press: root.wordScreen(7)

""")

class CButton(Button):
    bg_color = Styles.primary_color
    def pressed(self):
        self.background_color = (self.bg_color[0], self.bg_color[1], self.bg_color[2], 0.5)

    def released(self):
        self.background_color = self.bg_color

class EdButton(Button):
    bg_color = Styles.primary_red_color


class MButton(Button):
    menu_color = Styles.menu_color
    def pressed(self):
        self.background_color = (self.menu_color[0], self.menu_color[1], self.menu_color[2], 0.5)

    def released(self):
        self.background_color = self.menu_color

class QButton(Button):
    menu_color = Styles.primary_fundo
    def pressed(self):
        self.background_color = (self.menu_color[0], self.menu_color[1], self.menu_color[2], 0.5)

    def released(self):
        self.background_color = self.menu_color

class CTextInput(TextInput):
    bg_color = Styles.textinput_bg

class SignupText(ButtonBehavior, Label):
    bg_color = Styles.primary_color

class MenuPalavra(BoxLayout):
    bg_color = Styles.primary_color
    word_color = Styles.primary_fundo