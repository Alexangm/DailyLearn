from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from styles import Styles
from mydatabase import Database
from login import Login

Builder.load_string("""
#: import CButton custom_widgets                    
#: import CTextInput custom_widgets                    
<Perfil>:
    name: 'Perfil'
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
                    text: 'Perfil'
                    halign: 'center'
                    font_name: 'robotomedium.ttf'
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
                size_hint_y: 0.105
                spacing: dp(-10)
                orientation: 'horizontal'
                canvas.before:
                    Color:
                        rgba: (root.bg_color )
                    Rectangle:
                        pos: self.pos
                        size: self.size

                BoxLayout:
                    size_hint_x: 0.05
                    
                BoxLayout:
                    size_hint_x: 0.54
                    BoxLayout:
                        orientation: 'vertical'
                        Label:
                            size_hint_y: 0.4
                            id: pnome
                            text: '    Magnus Carlsen'
                            halign: 'left'
                            font_name: 'robotolight.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '34sp'
                            color: (0.9, 0.9, 1, 1)
                        Label:
                            size_hint_y: 0.3
                            id: pemail
                            text: '    MagzyBogues'
                            halign: 'left'
                            font_name: 'robotolightitalic.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '20sp' 
                            color: (0.9, 0.9, 1, 1)
                            italic: True
                        Label:
                            size_hint_y: 0.3
                
                BoxLayout:
                    orientation: 'vertical'
                    size_hint: 0.18, 0.9
                    Button:
                        size_hint_y: 0.95
                        on_press: root.switchToEdit()
                        background_normal: 'edit.png'
                    BoxLayout:
                        size_hint_y: 0.05    
                BoxLayout:
                    orientation: 'vertical'
                    size_hint: 0.18, 0.9
                    Button:
                        size_hint_y: 0.95
                        on_press: root.quit()
                        background_normal: 'sair.png'
                    BoxLayout:
                        size_hint_y: 0.05  




            BoxLayout:
                size_hint_y: 0.790
                orientation: 'vertical'
                spacing: dp(-15)

                BoxLayout:
                    size_hint_y: 0.125
                    orientation: 'horizontal'
                    canvas.before:
                        Color:
                            rgba: root.word_color
                        RoundedRectangle:
                            pos: (self.pos[0]+dp(12), self.pos[1]+dp(10))
                            size: (self.size[0]*0.95, self.size[1]*0.70)

                    BoxLayout:
                        size_hint_x: 0.10
                    BoxLayout:
                        size_hint_x: 0.70
                        Label:
                            id: lb1
                            text: 'Favoritas (17)'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '24sp'

                    Button:
                        size_hint: 0.15, 0.95
                        valign: 'top'
                        id: down
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
                            pos: (self.pos[0]+dp(12), self.pos[1]+dp(10))
                            size: (self.size[0]*0.95, self.size[1]*0.70)

                    BoxLayout:
                        size_hint_x: 0.10
                    BoxLayout:
                        size_hint_x: 0.70
                        Label:
                            id: lb2
                            text: 'Já conhecia (27)'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '24sp'

                    Button:
                        size_hint: 0.15, 0.95
                        valign: 'top'
                        id: down
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
                            pos: (self.pos[0]+dp(12), self.pos[1]+dp(10))
                            size: (self.size[0]*0.95, self.size[1]*0.70)

                    BoxLayout:
                        size_hint_x: 0.10
                    BoxLayout:
                        size_hint_x: 0.70
                        Label:
                            id: lb3
                            text: 'Conheci aqui (34)'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '24sp'

                    Button:
                        size_hint: 0.15, 0.95
                        valign: 'top'
                        id: down
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
                            pos: (self.pos[0]+dp(12), self.pos[1]+dp(10))
                            size: (self.size[0]*0.95, self.size[1]*0.70)

                    BoxLayout:
                        size_hint_x: 0.10
                    BoxLayout:
                        size_hint_x: 0.70
                        Label:
                            id: lb4
                            text: 'Já sabia o significado (18)'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '24sp'

                    Button:
                        size_hint: 0.15, 0.95
                        valign: 'top'
                        id: down
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
                            pos: (self.pos[0]+dp(12), self.pos[1]+dp(10))
                            size: (self.size[0]*0.95, self.size[1]*0.70)

                    BoxLayout:
                        size_hint_x: 0.10
                    BoxLayout:
                        size_hint_x: 0.70
                        Label:
                            id: lb5
                            text: 'Aprendi aqui (11)'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '24sp'

                    Button:
                        size_hint: 0.15, 0.95
                        valign: 'top'
                        id: down
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
                            pos: (self.pos[0]+dp(12), self.pos[1]+dp(10))
                            size: (self.size[0]*0.95, self.size[1]*0.70)

                    BoxLayout:
                        size_hint_x: 0.10
                    BoxLayout:
                        size_hint_x: 0.70
                        Label:
                            id: lb6
                            text: 'Quiz acertadas (36)'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '24sp'

                    Button:
                        size_hint: 0.15, 0.95
                        valign: 'top'
                        id: down
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
                            pos: (self.pos[0]+dp(12), self.pos[1]+dp(10))
                            size: (self.size[0]*0.95, self.size[1]*0.70)

                    BoxLayout:
                        size_hint_x: 0.10
                    BoxLayout:
                        size_hint_x: 0.70
                        Label:
                            id: lb7
                            text: 'Quiz erradas (20)'
                            halign: 'left'
                            font_name: 'robotomedium.ttf'
                            text_size: self.width, None
                            size: self.texture_size
                            font_size: '24sp'

                    Button:
                        size_hint: 0.15, 0.95
                        valign: 'top'
                        id: down
                        size: self.size
                        background_normal: 'next.png'
                        on_press: root.wordScreen(7)
                BoxLayout:
                    size_hint_y: 0.125 





""")

class Perfil(Screen):
    word = 'tela perfil, mudar'
    nome = None
    id = None
    email = None

    titulo = ''
    palavras = ''


    def changeRightTo(self):
        print('eu sou o self', Perfil.tela, Perfil.tela.name)
        #Screen.manager.current = 'Home'

    @staticmethod
    def getWord():
        return Perfil.word
    bg_color = Styles.primary_color
    word_color = Styles.primary_fundo

    def on_pre_enter(self, *args):
        Perfil.nome = Database.selectNameById(Login.id_user)
        Perfil.email = Login.getEmail()
        Perfil.id = Login.id_user
        #palavras = Draw()
        self.ids.pnome.text = Perfil.nome
        self.ids.pemail.text = Perfil.email
        self.ids.lb1.text = f'Favoritas ({Database.selectFavs(Perfil.id)})'
        self.ids.lb2.text = f'Já conhecia ({Database.selectKnew(Perfil.id)})'
        self.ids.lb3.text = f'Conheci aqui ({Database.selectConheciAqui(Perfil.id)})'
        self.ids.lb4.text = f'Já sabia o significado ({Database.selectSabia(Perfil.id)})'
        self.ids.lb5.text = f'Aprendi aqui ({Database.selectLearnHere(Perfil.id)})'
        self.ids.lb6.text = f'Quiz acertadas ({Database.selectQuizAcertos(Perfil.id)})'
        self.ids.lb7.text = f'Quiz erradas ({Database.selectQuizErros(Perfil.id)})'


    def addFav(self):
        pass

    def wordScreen(self, num):
        if num == 1:   
            Perfil.palavras = Database.selectFavsWords(Perfil.id)
            Perfil.titulo = 'Favoritas'
        if num == 2:   
            Perfil.palavras = Database.selectKnewWords(Perfil.id)
            Perfil.titulo = 'Já conhecia'
        if num == 3:   
            Perfil.palavras = Database.selectConheciAquiWords(Perfil.id)
            Perfil.titulo = 'Conheci aqui'
        if num == 4:   
            Perfil.palavras = Database.selectSabiaWords(Perfil.id)
            Perfil.titulo = 'Sabia o significado'
        if num == 5:   
            Perfil.palavras = Database.selectLearnHereWords(Perfil.id)
            Perfil.titulo = 'Aprendi aqui'
        if num == 6:   
            Perfil.palavras = Database.selectQuizAcertoWords(Perfil.id)
            Perfil.titulo = 'Quiz acertadas'
        if num == 7:   
            Perfil.palavras = Database.selectQuizErroWords(Perfil.id)
            Perfil.titulo = 'Quiz erradas'
        self.manager.transition.direction = 'left'
        self.manager.current = 'Album'




    def printValues(self):
        print('next', self.ids.next.pos)
        print('sound', self.ids.sound.pos)

    def goToMenu(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Home'

    def quit(self):
        self.manager.transition.direction = 'right'
        self.manager.current='login'
    
    def switchToEdit(self):
        self.manager.transition.direction = 'left'
        self.manager.current='edit'

