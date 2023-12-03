from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
from mydatabase import Database
from styles import Styles
from home import Home

from gtts import gTTS

Builder.load_string("""
#: import CButton custom_widgets                    
#: import CTextInput custom_widgets                    
<Palavra>:
    canvas.before:
        Color:
            rgba: 0.7, 0.78, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size       

    name: 'Palavra'
    FloatLayout:
        BoxLayout:
            orientation: 'vertical'
            BoxLayout: 
                size_hint_y: 0.105
                canvas.before:
                    Color:
                        rgba: (root.bg_color )
                    Rectangle:
                        pos: self.pos
                        size: self.size
                # height: dp(60)
                AnchorLayout:
                    size_hint: 0.001, 1.0
                    padding: [0, 0, dp(10), 0]
                    anchor_x: 'left'
                    Button: 
                        canvas.before:
                            Rectangle: 
                                pos: (self.pos[0]+dp(12), self.pos[1])
                                size: self.size
                                source: 'dl.png'
                        size_hint: None, None
                        size: dp(50), dp(50)
                        background_normal: ''
                        background_color: 0, 0, 0, 0
                        on_press: root.goToMenu()
                Label:
                    id: titulo
                    text: 'Serendipity'
                    halign: 'center'
                    font_name: 'robotoblack.ttf'
                    font_size: '40sp'
                    size_hint: 1.0, 1.0
                AnchorLayout:
                    size_hint: 0.001, 1.0
                    padding: [0, 0, dp(10), 0]
                    anchor_x: 'right'
                    Button: 
                        canvas.before:
                            Rectangle: 
                                pos: self.pos
                                size: self.size
                                source: 'menu.png'
                        id: menu
                        size_hint: None, None
                        size: dp(50), dp(50)
                        background_normal: ''
                        background_color: 0, 0, 0, 0
                        on_press: app.show_menu(menu)
            #titulo ^        
            
            BoxLayout:
                size_hint_y: 0.895
                canvas.before:
                    Color:
                        rgba: root.div
                    RoundedRectangle:
                        pos: (self.pos[0]+dp(12), self.pos[1]+dp(12))
                        # pos: self.pos
                        #size: self.size
                        size: (self.size[0]*0.95, self.size[1]*0.97)
                orientation: 'vertical'

                BoxLayout:
                    size_hint_y: 0.004
                        
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: 0.090
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound
                        background_normal: 'play.png'
                        on_press: root.reproduceSound()
                        halign: 'left'
                        valign: 'center'
                    BoxLayout:
                        size_hint_x: 0.70
                        Label:
                            id: traducao
                            text: 'Serendipidade'
                            halign: 'left'
                            valign: 'center'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: star
                        halign: 'right'
                        valign: 'center'
                        background_normal: 'star.png'
                        on_press: root.linkProfileAndWord()    

                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: 0.695
                    canvas.before:
                        Color:
                            rgba: root.meaning
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(24), self.pos[1]+dp(12))
                            # pos: self.pos
                            #size: self.size
                            size: (self.size[0]*0.90, self.size[1]*0.98)
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: 0.93
                        ScrollView:
                            do_scroll_y: True
                            Label:
                                id: significado
                                size_hint_y: None
                                halign: 'left'
                                valign: 'center'
                                height: self.texture_size[1]
                                text_size: self.width, None
                                padding: [dp(30),dp(10)]
                                font_name: 'robotomedium.ttf'  
                                font_size: '24sp'
                    BoxLayout:
                        size_hint_y: 0.07
                    
                
                BoxLayout:
                    size_hint_y: 0.05
                    orientation: 'horizontal'
                    height: dp(60)  # Defina a altura do layout conforme necessário
                    padding: dp(5)  # Adiciona margens à esquerda e à direita do BoxLayout
                    padding_top: dp(10)
                    spacing: dp(8)
                    BoxLayout:
                        size_hint_x: 0.1
                    BoxLayout:
                        size_hint_x: 0.8
                        spacing: dp(10)
                        ToggleButton:
                            id: option1
                            group: 'options'
                            state: 'down'
                            text: 'Português'
                            on_press: root.on_checkbox_active(option1, 1)

                        ToggleButton:
                            id: option2
                            group: 'options'
                            state: 'normal'
                            text: 'Inglês'
                            on_press: root.on_checkbox_active(option2, 2)
                    BoxLayout:
                        size_hint_x: 0.1

                    

                    
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: 0.161
                    size: self.minimum_size
                    padding: [dp(20),dp(20)]
                    #BoxLayout:
                       # size_hint_y: 0.15
                    
                    BoxLayout:
                        size_hint_y: 0.15
                        orientation: 'horizontal'
                        BoxLayout:
                            size_hint_x: 0.05
                            CheckBox:
                                id: b1
                                group: 'seriea'
                                on_active: root.changeProfile(self, 1, 1)
                                width: dp(50)  # Define a largura da CheckBox como 40dp
                                pos_hint: {'x': 0.1}

                        BoxLayout:
                            size_hint_x: 0.95
                            Label:
                                size_hint: None, 1
                                size: self.texture_size
                                text: 'Conhecia a palavra e sabia o significado!'
                                font_size: '19sp'
                                halign: 'left'
                                valign: 'center'


                    BoxLayout:
                        size_hint_y: 0.15
                        orientation: 'horizontal'
                        BoxLayout:
                            size_hint_x: 0.05
                            CheckBox:
                                id: b2
                                group: 'seriea'
                                on_active: root.changeProfile(self, 1, 0)
                                width: dp(60)  # Define a largura da CheckBox como 40dp
                                pos_hint: {'x': 0.1}
                        BoxLayout:
                            size_hint_x: 0.95
                            Label:
                                size_hint: None, 1
                                size: self.texture_size
                                text: 'Conhecia essa palavra, mas não o significado!'
                                font_size: '19sp'
                                halign: 'left'
                                valign: 'center'

                
                    BoxLayout:
                        size_hint_y: 0.15
                        orientation: 'horizontal'
                        BoxLayout:
                            size_hint_x: 0.05
                            CheckBox:
                                group: 'seriea'
                                id: b3
                                on_active: root.changeProfile(self, 0, 0)
                                width: dp(70)  # Define a largura da CheckBox como 40dp
                                pos_hint: {'x': 0.1}
                        BoxLayout:
                            size_hint_x: 0.95
                            Label:
                                size_hint: None, 1
                                size: self.texture_size
                                text: 'Não conhecia a palavra.'
                                font_size: '19sp'
                                halign: 'left'
                                valign: 'center'



""")


class Palavra(Screen):
    word = ''
    id_word = ''
    id_user = ''
    teste = ''

    significado_pt = ''
    significado_en = ''
    audio = ''
    traducao = ''

    bg_color = Styles.primary_color
    div = Styles.primary_fundo
    meaning = Styles.meaning_color


    def on_pre_enter(self, *args):
        Palavra.id_user = Home.id_user
        Palavra.id_word = Home.id_word
        temp = Database.selectWordKnoledge(Palavra.id_user, Palavra.id_word)
        if(temp == 1):
            self.ids.b1.active = True
        if(temp == 2):
            self.ids.b2.active = True
        if(temp == 3):
            self.ids.b3.active = True
        Palavra.word = Home.word
        Palavra.significado_pt = ''
        for a in Home.significado_pt:
            Palavra.significado_pt = Palavra.significado_pt + a + '\n'
        
        Palavra.significado_en = ''
        for b in Home.significado_en.values():
            Palavra.significado_en = Palavra.significado_en + b + '\n'
        
        Palavra.audio = Home.audio
        Palavra.traducao = Home.traducao
        self.ids.significado.text = Palavra.significado_pt
        self.ids.titulo.text = Palavra.word
        self.ids.traducao.text = Palavra.traducao.capitalize()

        if Database.isFav(Home.id_user, Home.id_word) == 1:
            self.ids.star.background_normal = 'starPress.png'
        else:
            self.ids.star.background_normal = 'star.png'

        self.ids.option2.state = 'normal'
        self.ids.option1.state = 'down'

    def on_checkbox_active(self, checkbox, value):

        if value == 1:
            self.ids.option2.state = 'normal'
            self.ids.option1.state = 'down'
            print('Valor 1,', Palavra.significado_pt)
            self.ids.significado.text = Palavra.significado_pt

        if value == 2:
            self.ids.option1.state = 'normal'
            self.ids.option2.state = 'down'
            print('Valor 2,', Palavra.significado_en)
            self.ids.significado.text = Palavra.significado_en
    
        print(self.ids.option1.state, self.ids.option2.state)
        print(self.ids.option1.size, self.ids.option2.size)

    def goToMenu(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Home'

    def linkProfileAndWord(self):
        if (self.ids.star.background_normal == 'star.png'):
            Database.linkWordWithProfile(Home.id_word, Home.id_user, 1)
            self.ids.star.background_normal = 'starPress.png'
        else: 
            Database.linkWordWithProfile(Home.id_word, Home.id_user, 0)
            self.ids.star.background_normal = 'star.png'

    def reproduceSound(self):
        #if self.ids.option2.state == 'down':
        #    texto = Palavra.word # + ' means...' + Palavra.significado_en
        #    tts = gTTS(text=texto, lang='en')
        #else:
        #    texto = Palavra.traducao #+ ' significa...' + Palavra.significado_pt
        #    tts = gTTS(text=texto, lang='pt')
        
        texto = Palavra.word
        tts = gTTS(text=texto, lang='en')
        tts.save("saida.mp3")
        sound = SoundLoader.load("saida.mp3")
        if sound:
            sound.play()
        
        print(Palavra.teste)

    def changeProfile(self, cb, conhecia, sabia):
        Palavra.teste += 'A'
        print(Palavra.id_word, Palavra.id_user, conhecia, sabia)
        Database.updateProfile(Palavra.id_word, Palavra.id_user, conhecia, sabia)
