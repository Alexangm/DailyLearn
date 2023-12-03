from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from mydatabase import Database
import re


Builder.load_string("""
#: import CButton custom_widgets
#: import CTextInput custom_widgets
#: import SignupText custom_widgets                                        
<Login>:
    name: 'login'
    canvas.before:
        Color:
            rgba: 0.3, 0.45, 0.7, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)

        BoxLayout:
            size_hint: 1.0, 0.04

        BoxLayout:
            size_hint: 1.0, 0.34
            Image:
                source: 'logo.png'
        BoxLayout:
            size_hint: 1.0, 0.07

        AnchorLayout:
            size_hint: 1.0, 0.45
            anchor_y: 'top'
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)
                padding: [dp(30), 0, dp(30), 0] 
                Label:
                    text: 'Acesse sua conta'
                    font_size: '16sp'
                    halign: 'center'
                    font_name: 'robotoblack.ttf'
                    text_size: self.size
                    size_hint_y: None
                    size: self.texture_size
                    color: 1, 1, 1, 1
                CTextInput:
                    id: email
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    hint_text: 'e-mail'
                CTextInput:
                    id: password
                    size_hint_y: None
                    height: dp(50)
                    password: True
                    multiline: False
                    hint_text: 'senha'
                CButton:
                    text: 'Entrar'
                    size_hint_y: None
                    height: dp(50)
                    on_press: root.login()
                Label:
                    id: msg
                    text: ''
                    color: 0.5, 0.1, 0.1, 1   
                    haling: 'left'
                    text_size: self.size
        AnchorLayout:
            size_hint: 1.0, 0.10
            anchor_x: 'center'
            BoxLayout:
                size_hint_x: None
                width: self.minimum_width
                Label:
                    text: 'Não possui uma conta?'
                    color: 1, 1, 1, 1
                    size_hint_x: None
                    size: self.texture_size

                SignupText:
                    text: ' Cadastre-se'
                    font_name: 'robotoblack.ttf'
                    size_hint_x: None
                    size: self.texture_size
                    on_press: root.switchToSignUp()                            
""")


def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        return True
    else:
        return False


class Login(Screen):
    email = None
    password = None
    id_user = None
    nome = None
    

    @staticmethod
    def getEmail():
        return Login.email
    

    @staticmethod
    def getPassword():
        return Login.password


    @staticmethod
    def getIduser():
        return Login.id_user
    

    @staticmethod
    def getNome():
        return Login.nome

    
    def login(self):
        Login.email = self.ids.email.text
        Login.password = self.ids.password.text
        if (Login.email == '' or Login.password == ''):
            self.ids.msg.text = 'Informações incompletas!'    
        else:
            if (is_valid_email(Login.email)):
                if(Database.isExist(Login.email, Login.password)):
                    #self.ids.msg.text = 'Logado com sucesso!'
                    Login.id_user = Database.selectIdFromEmail(Login.email)
                    Login.nome = Database.selectNameFromEmail(Login.email)
                    self.manager.transition.direction = 'left'
                    self.manager.current = 'Home' 
                else:
                    self.ids.msg.text = 'Email e/ou senha incorretos!'
            else:
                self.ids.msg.text = 'Email inválido!'


    def switchToSignUp(self):
        self.manager.transition.direction = 'left'
        self.manager.current='signup'


    def on_pre_enter(self, *args):
        self.ids.email.text = ''
        self.ids.password.text = ''
        self.ids.msg.text = ''
        Login.email = None
        Login.password = None
        Login.id_user = None
        Login.nome = None
