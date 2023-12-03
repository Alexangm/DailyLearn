from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
from styles import Styles
from utils import Draw
from mydatabase import Database
from login import Login
from utils import API_request
from gtts import gTTS


Builder.load_string("""
#: import CButton custom_widgets                    
#: import CTextInput custom_widgets                    
<Home>:
    name: 'Home'
    canvas.before:
        Color:
            rgba: 0.7, 0.78, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

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
                    text: 'Palavras'
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
            BoxLayout:
                size_hint_y: 0.009

            BoxLayout:
                size_hint_y: 0.727
                orientation: 'vertical'
                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1])
                            size: (self.size[0]*0.95, self.size[1]*0.90)
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound0
                        background_normal: 'play.png'
                        on_press: root.reproduceSound(0)
                    BoxLayout:
                        size_hint_x: 0.50
                        Label:
                            id: p0
                            text: 'abandoned'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: s0
                        background_normal: 'star.png'    
                        on_press: root.linkProfileAndWord(0)
                    Button:
                        size_hint: 0.15, 0.95
                        size: self.size
                        on_press: root.wordScreen(0)
                        background_normal: 'next.png'

                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1])
                            size: (self.size[0]*0.95, self.size[1]*0.90)
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound1
                        background_normal: 'play.png'
                        on_press: root.reproduceSound(1)
                    BoxLayout:
                        size_hint_x: 0.50
                        Label:
                            id: p1
                            text: 'abandoned'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: s1
                        background_normal: 'star.png'    
                        on_press: root.linkProfileAndWord(1)
                    Button:
                        size_hint: 0.15, 0.95
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(1)

                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1])
                            size: (self.size[0]*0.95, self.size[1]*0.90)
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound
                        background_normal: 'play.png'
                        on_press: root.reproduceSound(2)
                        
                    BoxLayout:
                        size_hint_x: 0.50
                        Label:
                            id: p2
                            text: 'abandoned'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: s2
                        background_normal: 'star.png'    
                        on_press: root.linkProfileAndWord(2)   
                    Button:
                        size_hint: 0.15, 0.95
                        id: star
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(2)

                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1])
                            size: (self.size[0]*0.95, self.size[1]*0.90)
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound
                        background_normal: 'play.png'
                        on_press: root.reproduceSound(3)
                    BoxLayout:
                        size_hint_x: 0.50
                        Label:
                            id: p3
                            text: 'abandoned'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: s3
                        background_normal: 'star.png'    
                        on_press: root.linkProfileAndWord(3)  
                    Button:
                        size_hint: 0.15, 0.95
                        id: star
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(3)

                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1])
                            size: (self.size[0]*0.95, self.size[1]*0.90)
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound
                        background_normal: 'play.png'
                        on_press: root.reproduceSound(4)
                    BoxLayout:
                        size_hint_x: 0.50
                        Label:
                            id: p4
                            text: 'abandoned'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: s4
                        background_normal: 'star.png'    
                        on_press: root.linkProfileAndWord(4) 
                    Button:
                        size_hint: 0.15, 0.95
                        id: star
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(4)

                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1])
                            size: (self.size[0]*0.95, self.size[1]*0.90)
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound
                        background_normal: 'play.png'
                        on_press: root.reproduceSound(5)
                    BoxLayout:
                        size_hint_x: 0.50
                        Label:
                            id: p5
                            text: 'abandoned'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: s5
                        background_normal: 'star.png'    
                        on_press: root.linkProfileAndWord(5)  
                    Button:
                        size_hint: 0.15, 0.95
                        id: star
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(5)

                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1])
                            size: (self.size[0]*0.95, self.size[1]*0.90)
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound
                        background_normal: 'play.png'
                        on_press: root.reproduceSound(6)
                    BoxLayout:
                        size_hint_x: 0.50
                        Label:
                            id: p6
                            text: 'abandoned'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '36sp'
                    Button:
                        size_hint: 0.15, 0.95
                        id: s6
                        background_normal: 'star.png'    
                        on_press: root.linkProfileAndWord(6)  
                    Button:
                        size_hint: 0.15, 0.95
                        id: star
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(6)

                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1])
                            size: (self.size[0]*0.95, self.size[1]*0.90)
                    Button:
                        size_hint: 0.15, 0.95
                        id: sound
                        background_normal: 'play.png'
                        on_press: root.reproduceSound(7)
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
                        on_press: root.linkProfileAndWord(7)  
                    Button:
                        size_hint: 0.15, 0.95
                        id: star
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(7)
            BoxLayout:
                size_hint_y: 0.009
        
            BoxLayout:
                size_hint_y: 0.15
""")


class Home(Screen):
    word = 'tela home, mudar'
    traducao = ''
    audios = []
    id_word = ''
    significado_pt = ''
    significado_en = ''
    id_palavras = ''
    stars = ''
    palavras = Draw()

    email = None
    senha = None
    id_user = None
    nome = None

    @staticmethod
    def getWord():
        return Home.word
    
    bg_color = Styles.primary_color
    word_color = Styles.primary_fundo


    def on_pre_enter(self, *args):
        Home.email = Login.getEmail()
        Home.senha = Login.getPassword()
        Home.id_user = Login.getIduser()
        Home.nome = Login.getNome()
        Home.id_palavras = self.ids.p0, self.ids.p1, self.ids.p2, self.ids.p3, self.ids.p4, self.ids.p5, self.ids.p6, self.ids.p7
        Home.stars = self.ids.s0, self.ids.s1, self.ids.s2, self.ids.s3, self.ids.s4, self.ids.s5, self.ids.s6, self.ids.s7
        palavras = Draw()
        
        print(palavras)
        for i, palavra in enumerate(palavras):
            iword = str(Database.selectWord(palavra)[0][0])
            Home.id_palavras[i].text = iword.capitalize()
            print(iword.capitalize())
            if Database.isFav(Home.id_user, Home.palavras[i]) == 1:
                Home.stars[i].background_normal = 'starPress.png'
            else:
                Home.stars[i].background_normal = 'star.png'


    def addFav(self):
        pass


    def linkProfileAndWord(self, idWord):
        if (Home.stars[idWord].background_normal == 'star.png'):
            Database.linkWordWithProfile(Home.palavras[idWord], Home.id_user, 1)
            Home.stars[idWord].background_normal = 'starPress.png'
        else: 
            Database.linkWordWithProfile(Home.palavras[idWord], Home.id_user, 0)
            Home.stars[idWord].background_normal = 'star.png'


    def wordScreen(self, idWord):
        Home.word = str(Database.selectWord(Draw()[idWord])[0][0]).capitalize()
        Home.id_word = Database.selectIdFromWord(Home.word.lower())
        print(Home.word.lower())
        dados = API_request(Home.word.lower())

        Home.audio = dados['audios']
        Home.significado_en = dados['definitions']
        Home.traducao = dados['traducao']
        Home.significado_pt = dados['portugues']

        Database.linkWWP(Home.palavras[idWord], Home.id_user)    
        self.manager.transition.direction = 'left'    
        self.manager.current = 'Palavra'


    def goToMenu(self):
        self.manager.current = 'Home'


    def reproduceSound(self, idWord):
        texto = Home.id_palavras[idWord].text
        tts = gTTS(text=texto, lang='en')
        tts.save("saida.mp3")

        sound = SoundLoader.load("saida.mp3")
        if sound:
            sound.play()
        Database.linkWWP(Home.palavras[idWord], Home.id_user)
