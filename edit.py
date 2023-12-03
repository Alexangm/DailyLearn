import re
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from mydatabase import Database
from perfil import Perfil
from styles import Styles
from kivy.uix.popup import Popup
from mydatabase import Database

Builder.load_string("""
#: import CTextInput custom_widgets
#: import CButton custom_widgets
<Edit>:
    name: 'edit'
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
                    id: email
                    font_size: '22sp'
                    size_hint_y: None
                    color: 1, 1, 1, 1   
                    halign: 'center'
                    text_size: self.size 
                    font_name: 'robotoblack.ttf'
                    size: self.texture_size
                CTextInput:
                    id: nome
                    hint_text: "nome"
                    text: ''
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                CTextInput:
                    id: senhaAtual
                    hint_text: 'senha atual'
                    max_length: 25
                    size_hint_y: None
                    password: True
                    height: dp(50)
                    multiline: False
                    on_text: root.name_check(self)
                CTextInput:
                    id: novaSenha
                    hint_text: 'nova senha'
                    size_hint_y: None
                    height: dp(50)
                    password: True
                    multiline: False
                    on_text: root.space_check(self)
                CTextInput:
                    id: cNovaSenha
                    hint_text: 'confirmar nova senha'
                    size_hint_y: None
                    height: dp(50)
                    password: True
                    multiline: False
                    on_text: root.space_check(self)
                EdButton:
                    text: 'Salvar'
                    background_color: root.blue
                    on_press: root.editData()
                    size_hint_y: None
                    height: dp(50)
                EdButton:
                    text: 'Cancelar'
                    on_press: root.switchToPerfil()
                    background_color: root.edit_color
                    size_hint_y: None
                    height: dp(50)
                EdButton:
                    text: 'Deletar conta'
                    on_press: root.delete()
                    background_color: root.delete_color
                    size_hint_y: None
                    height: dp(50)
                Label:
                    id: msgErro
                    text: ''
                    color: 0.3, 0, 0, 1   
                    haling: 'left'
                    text_size: self.size 
                    font_name: 'robotolight.ttf'

<Popup>:
    title: 'Tem certeza que deseja apagar a conta?'
    title_align: 'center'
    title_size: '28sp'
    size_hint: 0.8, 0.38
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y: 0.7
            orientation: 'vertical'
            Label:
                id: confirm
                text: 'Confirme sua senha:'
                color: 1, 1, 1, 1   
                haling: 'left'
                font_size: '20sp'
                font_name: 'robotolight.ttf'
            CTextInput:
                id: confirmPassword
                hint_text: 'senha'
                max_length: 25
                size_hint_y: None
                height: dp(50)
                multiline: False
                password: True  
            Label:
                id: msgPop
                text: ''
                color: 0.9, 0.9, 0.9, 1   
                haling: 'left'
                font_size: '16sp'
                font_name: 'robotolight.ttf'                 
        BoxLayout:
            size_hint_y: 0.3
            orientation: 'horizontal'
            Button:
                text: 'Não'
                on_press: root.dismiss()
                font_size: '18sp'
                size_hint: 0.5, 0.7
            Button:
                text: 'Sim'
                font_size: '18sp'
                on_press: root.deleteAcc()
                size_hint: 0.5, 0.7           
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


class popup(Popup):
    tela = ''
    delete_color = Styles.delete_red_color
    idUser = ''
    def deleteAcc(self):
        popup.idUser = Edit.idUser
        if(self.ids.confirmPassword.text == Database.selectPasswordFromId(popup.idUser)):
            Database.deleteUser(popup.idUser)
            self.dismiss()
            popup.tela.manager.current = 'login'
        else:
            self.ids.msgPop.text = 'Senha incorreta.'
            

class Edit(Screen):
    delete_color = Styles.delete_red_color
    edit_color = Styles.edit_color
    blue = Styles.primary_color
    idUser = ''
    password = ''

    def on_pre_enter(self, *args):
        Edit.idUser = Perfil.id
        self.ids.email.text = Perfil.email
        self.ids.nome.text = Perfil.nome
        self.ids.senhaAtual.text = ''
        self.ids.novaSenha.text = ''
        self.ids.cNovaSenha.text = ''


    def name_check(self, text_input):
        if(len(text_input.text) > 25):
            text_input.text = text_input.text[:-1]


    def space_check(self, text_input):
        text_input.text = text_input.text.replace(" ", "")


    def switchToPerfil(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Perfil'


    def delete(self):
        popup.tela = self
        popup().open()

    
    def editData(self):
        nome = self.ids.nome.text
        senhaAtual = self.ids.senhaAtual.text
        novaSenha = self.ids.novaSenha.text
        cNovaSenha = self.ids.cNovaSenha.text

        if novaSenha or cNovaSenha:
            if senhaAtual == Database.selectPasswordFromId(Edit.idUser):
                if novaSenha == cNovaSenha:
                    if len(novaSenha) > 7:
                        if nome:
                            Database.changeUser(Edit.idUser, nome, novaSenha)
                            self.manager.transition.direction = 'left'
                            self.manager.current = 'Perfil'
                        else:
                            Database.changePassword(Edit.idUser, novaSenha)
                            self.manager.transition.direction = 'left'
                            self.manager.current = 'Perfil'
                    else:
                        self.ids.msgErro.text = 'Nova senha deve ter pelo menos 8 caracteres.'
                else:
                    self.ids.msgErro.text = 'Senhas não coincidem!'
            else:
                self.ids.msgErro.text = 'Senha incorreta!'
        elif nome:
            if senhaAtual == Database.selectPasswordFromId(Edit.idUser):
                Database.changeName(Edit.idUser, nome)
                self.manager.transition.direction = 'left'
                self.manager.current = 'Perfil'
            else:
                self.ids.msgErro.text = 'Senha incorreta!'
        else:
            self.ids.msgErro.text = 'Informações incompletas!'
