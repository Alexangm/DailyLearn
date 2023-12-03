import random
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from mydatabase import Database
from styles import Styles
from kivy.core.window import Window
from kivy.properties import NumericProperty
from utils import DrawQuiz, DrawQuizOptions, traduzir_com_linguee
from login import Login
#from home import Home

#from gtts import gTTS

Builder.load_string("""
#: import CButton custom_widgets                    
#: import CTextInput custom_widgets                    
<Quiz>:
    canvas.before:
        Color:
            rgba: 0.7, 0.78, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size       

    name: 'Quiz'
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
                size_hint_y: 0.895
                canvas.before:
                    Color:
                        rgba: root.div
                    RoundedRectangle:
                        pos: (root.x*0.015, root.y*0.74)
                        size: (root.x * 0.57, root.y*0.60)
                orientation: 'vertical'
                BoxLayout:
                    size_hint_y: 0.040   
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: 0.032
                    BoxLayout:
                        orientantion: 'horizontal'
                        Label:
                            id: titulo
                            text: '            Qual a tradução de:'
                            halign: 'center'
                            valign: 'center'
                            font_name: 'robotomedium.ttf'
                            font_size: '28sp'
                            size_hint: 1.0, 1.0
                        Label:
                            id: score
                            text: '4/5'
                            halign: 'right'
                            valign: 'top'
                            font_name: 'robotomedium.ttf'
                            font_size: '22sp'
                            size_hint: 0.2, 1.0
                BoxLayout:
                    size_hint_y: 0.030  
                BoxLayout:
                    size_hint_y: 0.042
                    Label:
                        id: palavra
                        text: 'Amiable'
                        halign: 'center'
                        valign: 'center'
                        font_name: 'robotomedium.ttf'
                        font_size: '50sp'
                        size_hint: 1.0, 1.0
                BoxLayout:
                    size_hint_y: 0.18
                    canvas.before:
                        Color:
                            id: bola
                            rgba: (1,1,1,root.ellipse_opacity)
                        Ellipse:
                            #pos: (self.pos[0]+dp(12), self.pos[1]+dp(12))
                            pos: (root.x*0.075, root.y*0.42)
                            size: (root.x * 0.45, root.y*0.20)

                    

                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: 0.15
                    size: self.minimum_size
                    padding: [dp(40),dp(-90)]
                    canvas.before:
                        Color:
                            rgba: root.meaning
                        Rectangle:
                            pos: (root.x*0.03, root.y*0.76)
                            size: (root.x * 0.54, root.y*0.35)
                    BoxLayout:
                        size_hint_y: 0.13
                        orientation: 'horizontal'
                        BoxLayout:
                            size_hint_x: 0.05
                            CheckBox:
                                id: o0
                                on_active: root.funcaoOpcao(self, 0)
                                group: 'grupo1'
                                width: dp(50)  # Define a largura da CheckBox como 40dp
                                pos_hint: {'x': 0.1}
                        BoxLayout:
                            size_hint_x: 0.95
                            Label:
                                id: l0
                                size_hint: None, 1
                                size: self.texture_size
                                text: ' Corredor'
                                font_size: '36sp'
                                halign: 'left'
                                valign: 'center'
                    BoxLayout:
                        size_hint_y: 0.13
                        orientation: 'horizontal'
                        BoxLayout:
                            size_hint_x: 0.05
                            CheckBox:
                                id: o1
                                on_active: root.funcaoOpcao(self, 1)
                                group: 'grupo1'
                                width: dp(60)  # Define a largura da CheckBox como 40dp
                                pos_hint: {'x': 0.1}
                                margin: [10, 10]
                        BoxLayout:
                            size_hint_x: 0.95
                            Label:
                                id: l1
                                size_hint: None, 1
                                size: self.texture_size
                                text: ' Alfinete'
                                font_size: '36sp'
                                halign: 'left'
                                valign: 'center'
                    BoxLayout:
                        size_hint_y: 0.13
                        orientation: 'horizontal'
                        BoxLayout:
                            size_hint_x: 0.05
                            CheckBox:
                                id: o2
                                on_active: root.funcaoOpcao(self, 2)
                                group: 'grupo1'
                                width: dp(70)  # Define a largura da CheckBox como 40dp
                                pos_hint: {'x': 0.1}
                        BoxLayout:
                            size_hint_x: 0.95
                            Label:
                                id: l2
                                size_hint: None, 1
                                size: self.texture_size
                                text: ' Amável'
                                font_size: '36sp'
                                halign: 'left'
                                valign: 'center'
                    BoxLayout:
                        size_hint_y: 0.13
                        orientation: 'horizontal'
                        BoxLayout:
                            size_hint_x: 0.05
                            CheckBox:
                                id: o3
                                on_active: root.funcaoOpcao(self, 3)
                                group: 'grupo1'
                                width: dp(70)  # Define a largura da CheckBox como 40dp
                                pos_hint: {'x': 0.1}
                        BoxLayout:
                            size_hint_x: 0.95
                            Label:
                                id: l3
                                size_hint: None, 1
                                size: self.texture_size
                                text: ' Juramento'
                                font_size: '36sp'
                                halign: 'left'
                                valign: 'center'
                    BoxLayout:
                        size_hint_y: 0.48
                
                BoxLayout:
                    size_hint_y: 0.11
                    
                BoxLayout:
                    size_hint_y: 0.04
                    Label:
                        id: retorno
                        text: 'Correto!'
                        halign: 'center'
                        valign: 'center'
                        color: root.divT 
                        font_name: 'robotomedium.ttf'
                        font_size: '55sp'
                        size_hint: 1.0, 1.0


                BoxLayout:
                    size_hint_y: 0.116

                BoxLayout:
                    size_hint_y: 0.04
                    Label:
                        id: resposta
                        text: 'A palavra era Amável!'
                        halign: 'center'
                        valign: 'center'
                        color: root.divT 
                        font_name: 'robotomedium.ttf'
                        font_size: '30sp'
                        size_hint: 1.0, 1.0
                
                BoxLayout:
                    size_hint_y: 0.2
                    MButton:
                        id: botaoProx
                        text: 'Próxima'
                        size_hint_y: None
                        border: (0, 0, 0, 0)
                        background_normal: ''  # Evita o fundo padrão do botão
                        background_color: rgba('#123456')  # Cor de fundo padrão
                        on_press: root.proxima()

                
                
""")

# PALAVRA EM INGLES > TRADUCAO
# LISTA PE 3 PALAVRAS PT ALEATORIAS

#LISTA OPCOES = ID.O1, ID.O2
#LISTA LABEL = 

""">> SORT UM 1-4
OPCERTA = 2 SALVEI NA OP 2 TRADUCAO == BOTAO2 V <> X

FOR 1234
    IF I <> OPCERTA
        LBI = PE[I]

CLICOU UMA DELAS ?
? CERTA 

? ERRADA

"""


class Quiz(Screen):
    x = Window.width
    y = Window.height
    ops = ''
    labs = ''

    word = ''
    id_word = ''
    id_user = ''
    significado_pt = ''
    significado_en = ''
    audio = ''
    traducao = ''

    bg_color = Styles.primary_color
    div = Styles.primary_fundo
    divT = Styles.primary_fundo
    meaning = Styles.meaning_color

    lista = ''
    palavraCorreta = ''
    opCerta = ''

    listaPalavras = DrawQuiz()
    listaNumerosQuiz = DrawQuizOptions()
    indexQuiz = 0

    acerto = 0
    erro = 0


    ellipse_opacity = NumericProperty(1)
    def on_pre_enter(self, *args):
        Quiz.id_user = Login.id_user
        if Quiz.acerto + Quiz.erro != 5:
            random.seed()
            Quiz.opCerta = random.randint(0, 3)

            Quiz.ops = self.ids.o0, self.ids.o1, self.ids.o2, self.ids.o3
            Quiz.labels = self.ids.l0, self.ids.l1, self.ids.l2, self.ids.l3
            
            Quiz.lista = ['Corredor', 'Alfinete', 'Juramento', 'Rabanete', 'Carro', 'Pindamonha', 'Garrafa', 'Quebrar', 'Sofrer', 'Mãe', 'Pai', 'Filho', 'Irmão', 'Cerveja', 'Tela', 
                'Teta', 'Veja', 'Vi', 'Verei', 'Verás', 'Vou', 'Cruzeiro', 'Vírus', 'Computador', 'Pessoa', 'Amaciante', 'Lula', 'Lento', 'Ladrão', 'Rabo', 'Homossexual', 'Hétero'
                , 'Adolescente', 'Corno']
            
            
            palavra_da_vez = Database.selectWordById(Quiz.listaPalavras[Quiz.indexQuiz]).capitalize()
            
            self.ids.palavra.text = palavra_da_vez
            self.ids.score.text = f'{Quiz.acerto + Quiz.erro + 1}/5'
            Quiz.palavraCorreta = traduzir_com_linguee(palavra_da_vez).capitalize()
            
            print('AQUI >>', Quiz.labels, Quiz.opCerta, Quiz.palavraCorreta)
            

            Quiz.labels[Quiz.opCerta].text = ' ' + Quiz.palavraCorreta

            indexPalavras = Quiz.indexQuiz * 3
            for i in range(4):
                if Quiz.opCerta != i:
                    Quiz.labels[i].text = ' ' + Database.selectPalavraPortugues(Quiz.listaNumerosQuiz[indexPalavras])
                    #print(Quiz.listaNumerosQuiz[indexPalavras], indexPalavras, '%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                    indexPalavras += 1
            print('preenter')
            Quiz.reset(self)

    def goToMenu(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Home'
        


    def funcaoOpcao(self, cb, num):
        if cb.active:
            Quiz.setBotao(self, num == Quiz.opCerta)
        for op in Quiz.ops:
            op.disabled = 1
    
    def reset(self):
        tativ = Quiz.acerto
        terro = Quiz.erro
        Quiz.r = 0
        for op in Quiz.ops:
            op.active = False
        Quiz.r = 1
        Quiz.acerto = tativ
        Quiz.erro = terro
        self.ids.retorno.text = ''
        self.ids.resposta.text = ''
        self.ellipse_opacity = 0

        self.ids.botaoProx.disabled = 1
        #self.ids.botaoProx.background_color = self.meaning

    def setBotao(self, certo):
        print(self, "entrou aqui mais uma vez")
        self.ellipse_opacity = 1  # Se 1, ellipse aparece; Se 0, ellipse some;
        self.ids.botaoProx.disabled = 0 if Quiz.indexQuiz < 4 else 1
        if certo:
            Quiz.acerto += 1
            print('id=',  Quiz.id_user, 'palavra=', Quiz.listaPalavras[Quiz.indexQuiz], 'fl=', 1)
            Database.linkWWP(Quiz.listaPalavras[Quiz.indexQuiz], Quiz.id_user)
            Database.insertQuiz(Quiz.id_user, Quiz.listaPalavras[Quiz.indexQuiz], 1)
            self.ids.retorno.text = 'Correto!'
            self.ids.resposta.text = 'Parabéns!'
        else:
            Quiz.erro += 1
            Database.linkWWP(Quiz.listaPalavras[Quiz.indexQuiz], Quiz.id_user)
            Database.insertQuiz(Quiz.id_user, Quiz.listaPalavras[Quiz.indexQuiz], 0)
            self.ids.retorno.text = 'Errado!'
            self.ids.resposta.text = f'A palavra era {Quiz.palavraCorreta}!'

        if Quiz.acerto + Quiz.erro == 5:
            act = 'acertos' if Quiz.acerto > 1 else 'acerto'
            err = 'erros' if Quiz.erro > 1 else 'erro'
            self.ids.resposta.text = f'{self.ids.resposta.text}\nVocê obteve {Quiz.acerto} {act}.'

            

    def proxima(self):
        Quiz.indexQuiz += 1
        if Quiz.indexQuiz > 4:
            self.ids.botaoProx.disabled = 1
            #self.ids.botaoProx.background_color = self.meaning
        else:
            Quiz.on_pre_enter(self)
            for op in Quiz.ops:
                op.disabled = 0
            
