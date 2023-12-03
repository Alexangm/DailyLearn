import re
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from mydatabase import Database

Builder.load_string("""
#: import CTextInput custom_widgets
#: import CButton custom_widgets
<Signup>:
    name: 'signup'
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
            size_hint: 1, 0.34
            Image:
                source: 'logo.png'
        BoxLayout:
            size_hint: 1, 0.07
        AnchorLayout:
            size_hint: 1, 0.55
            anchor_y: 'top'           
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                spacing: dp(10)
                height: self.minimum_height
                padding: [dp(30), 0, dp(30), 0] 
                Label:
                    text: 'Crie sua conta'
                    font_size: '16sp'
                    size_hint_y: None
                    color: 1, 1, 1, 1   
                    halign: 'left'
                    text_size: self.size 
                    font_name: 'robotoblack.ttf'
                    size: self.texture_size
                CTextInput:
                    id: email
                    hint_text: "email"
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    on_text: root.space_check(self)
                CTextInput:
                    id: name
                    hint_text: 'nome'
                    max_length: 25
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    on_text: root.name_check(self)

                CTextInput:
                    id: password
                    hint_text: 'senha'
                    size_hint_y: None
                    height: dp(50)
                    password: True
                    multiline: False
                    on_text: root.space_check(self)
                CTextInput:
                    id: cpassword
                    hint_text: 'confirmar senha'
                    size_hint_y: None
                    height: dp(50)
                    password: True
                    multiline: False
                    on_text: root.space_check(self)
                CButton:
                    text: 'Criar conta'
                    on_press: root.createEntry()
                    size_hint_y: None
                    height: dp(50)
                Label:
                    id: msg
                    text: ''
                    color: 0.3, 0, 0, 1   
                    haling: 'left'
                    text_size: self.size 
                    font_name: 'robotolight.ttf'
""")


def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        return True
    else:
        return False


def is_valid_password(password):
    # Define a expressão regular para verificar se a senha tem pelo menos 8 caracteres
    regex = r'^.{8,}$'
    
    # Verifica se a senha corresponde ao padrão da expressão regular
    if re.match(regex, password):
        return True
    else:
        return False
    



    

class Signup(Screen):
    def on_pre_enter(self, *args):
        self.ids.email.text = ''
        self.ids.name.text = ''
        self.ids.password.text = ''
        self.ids.cpassword.text = ''

    def createEntry(self):
        email = self.ids.email.text
        name = self.ids.name.text
        password = self.ids.password.text
        cpassword = self.ids.cpassword.text
        if (email == '' or password == '' or name =='' or cpassword == ''):
            self.ids.msg.text = 'Informações incompletas!'
        else: 
            if(is_valid_email(email)):
                if(is_valid_password(password)):
                    if(password == cpassword):
                        if(Database.isValid(email)):
                            Database.insertdata(email, name, password)
                            self.manager.transition.direction = 'right'
                            self.manager.current = 'login'
                        else:
                            self.ids.msg.text = 'Email já cadastrado!'
                    else:
                        self.ids.msg.text = 'As senhas não coincidem!'
                else:
                    self.ids.msg.text = 'A senha deve ter pelo menos 8 caracteres.'

                
            else:
                self.ids.msg.text = 'O email não é válido!'


    def name_check(self, text_input):
        #text_input.text = text_input.text.replace(" ", "")
        if(len(text_input.text) > 25):
            text_input.text = text_input.text[:-1]

    def space_check(self, text_input):
        text_input.text = text_input.text.replace(" ", "")