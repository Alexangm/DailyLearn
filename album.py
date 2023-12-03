from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from mydatabase import Database
from styles import Styles
from custom_widgets import QButton
from home import Home
from utils import API_request
from perfil import Perfil


Builder.load_string("""
#: import CButton custom_widgets                    
#: import CTextInput custom_widgets                    
<Album>:
    canvas.before:
        Color:
            rgba: 0.7, 0.78, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size       

    name: 'Album'
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
                                source: 'DL.png'
                        size_hint: None, None
                        size: dp(50), dp(50)
                        background_normal: ''
                        background_color: 0, 0, 0, 0
                        on_press: root.goToMenu()
                Label:
                    id: titulo
                    text: 'Quiz'
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
                size_hint_y: 0.02 
            BoxLayout: 
                size_hint_y: 0.775
                BoxLayout:
                    orientation: 'horizontal'
                    BoxLayout: 
                        size_hint_x: 0.05 
                    ScrollView:
                        do_scroll_y: True
                        h_align: 'center'
                        bar_width: 0
                        size_hint: 0.9, 1
                        GridLayout:
                            spacing: dp(20)
                            id: role
                            cols: 1
                            size_hint_y: None
                            height: self.minimum_height
                    BoxLayout: 
                        size_hint_x: 0.05 
                        
            BoxLayout: 
                size_hint_y: 0.1    
""")


class Album(Screen):
    bg_color = Styles.primary_color
    div = Styles.primary_fundo
    divT = Styles.primary_fundo
    meaning = Styles.meaning_color
    bg_color = Styles.primary_color
    word_color = Styles.primary_fundo

    word_list = None
    botoes_list = []

    def on_pre_enter(self, *args):
        self.ids.titulo.text = Perfil.titulo
        if Album.word_list != 0:
            for btn in Album.botoes_list:
                self.ids.role.remove_widget(btn)
        if (Perfil.palavras) != 0:
            Album.word_list = sorted(Perfil.palavras)
            for i in range(len(Album.word_list)):
                self.generate(Album.word_list[i])
                

    def generate(self, palavra):
        # BoxLayout externa
        btn = QButton(text=palavra)
        btn.bind(on_press=lambda instance: Album.switchToPalavra(self, palavra))
        Album.botoes_list.append(btn)
        self.ids.role.add_widget(btn)

    
    def switchToPalavra(self,palavra):
        Home.word = palavra
        Home.id_word = Database.selectIdFromWord(Home.word.lower())
        print(Home.word.lower())
        dados = API_request(Home.word.lower())

        Home.audio = dados['audios']
        Home.significado_en = dados['definitions']
        Home.traducao = dados['traducao']
        Home.significado_pt = dados['portugues']
        self.manager.transition.direction = 'left'
        self.manager.current = 'Palavra'
        
        
    def goToMenu(self):
        self.manager.current = 'Home'
        self.manager.transition.direction = 'right'
