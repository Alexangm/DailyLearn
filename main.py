from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from login import Login
from signup import Signup
from mydatabase import Database
from home import Home
from palavra import Palavra
from perfil import Perfil
from quiz import Quiz
from album import Album
from kivy.uix.dropdown import DropDown
from edit import Edit


Window.softinput_mode="below_target"
Window.size = (480, 912)

class Interface(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            Database.ConnectDatabase()
        except Exception as e:
            print('aqui fora')
            print(e)

        home = Home()
        login = Login()
        signup = Signup()
        palavra = Palavra()
        perfil = Perfil()
        quiz = Quiz()
        album = Album()
        edit = Edit()
        self.add_widget(login)
        self.add_widget(signup)
        self.add_widget(home)
        self.add_widget(palavra)
        self.add_widget(perfil)
        self.add_widget(quiz)
        self.add_widget(album)
        self.add_widget(edit)


class DropdownMenu(DropDown):
    def changeTo(self, where):
        English.dropdown.dismiss()
        App.get_running_app().root.transition.direction = 'left'
        App.get_running_app().root.current= where
    

class English(App):  # mesmo nome que o .kv
    dropdown = None
    def show_menu(self, id):
        English.dropdown = DropdownMenu()
        English.dropdown.open(id)


English().run()
#Database.ConnectDatabase()
#print(Database.selectIdFromWord("Suave"))
#Database.updateWord(486, "Strain")
#Database.droppalavrasQuiz()

#listaEN = ["Pretend","Prejudice","College","Library","Support","Intend","Lunch","Devolve","Mayor","Anthem","Parents","Costume","Eventually","Exit","Fabric","Lecture","Novel","Application","Attend","Pasta","Sensible","Realize","Shoot","Actually","Pull","Baton","Enroll","Push","Convict","Tax","Coroner","Patron","Foosball","Genial","Valorous"]

#for palavra in listaEN:
    #print(palavra)
    #Database.insertWord(palavra)


#listaPT = ["Aconselhar", "Agredir", "Ajudar", "Almejar", "Anular", "Aprovar", "Argumentar", "Atender", "Avaliar", "Celebrar", "Cometer", "Comprar", "Conduzir", "Conectar", "Confundir", "Conquistar", "Construir", "Contribuir", "Conversar", "Convocar", "Corrigir", "Cultivar", "Declarar", "Descrever", "Desejar", "Destruir", "Desvendar", "Dialogar", "Dificultar", "Diversificar", "Divulgar", "Dominar", "Elaborar", "Embelezar", "Empregar", "Encontrar", "Enganar", "Enriquecer", "Entender", "Estudar", "Evoluir", "Exigir", "Explorar", "Expressar", "Fomentar", "Fortalecer", "Frequentar", "Impressionar"]
