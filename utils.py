import random
from datetime import date
import requests
from bs4 import BeautifulSoup

#SORTEIOS
def Draw():
    seed_day = int(f'{date.today().year}{date.today().month}{date.today().day}')
    random.seed(seed_day)
    return sorted(random.sample(range(531), 8))


def DrawQuiz():
    seed_yesterday = int(f'{date.today().year}{date.today().month}{date.today().day-1}')
    random.seed(seed_yesterday)
    numeros = sorted(random.sample(range(566), 8))
    return [numeros[0], numeros[1], numeros[3], numeros[5], numeros[7]]

#for i in range(101,1000):
#    if DrawQuiz(i)[3] > 531:
#        print(i, DrawQuiz(i))


def DrawQuizOptions():
    seed_yesterday = int(f'{date.today().year}{date.today().month}{date.today().day-1}')
    random.seed(seed_yesterday)
    lista = random.sample(range(423), 15)
    #lista.pop()
    #lista.append(99)
    return lista


#PALAVRAS
def API_request(word):
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
    response = requests.get(url + word)
    
    if response.status_code == 200:
        api_dados = response.json()
        dados = {}
        dado = api_dados[0]
        dados["word"] = dado["word"]
        #dados["phonetic"] = dado['phonetic']
        for phonetics in dado['phonetics']:
            if (phonetics['audio'] == ''):
                pass
            dados["audios"] = phonetics['audio']
        dados["definitions"] = {}
        dados["synonyms"] = {}
        dados["antonyms"] = {}
        i = 0
        for definicao in dado['meanings'][0]['definitions']:
            i += 1
            dados["definitions"][str(i)] = str(i) + '. ' + definicao['definition']
        traducao = traduzir_com_linguee(word) 
        dados["traducao"] = traducao      
        dados["portugues"] = spans(traducao)

        return dados
    else:
        print(word, "Não encontrada!")
        return 0


def spans(word):
    cword = remover_acentos_manual(word)
    url = f"https://www.dicio.com.br/{cword}"
    resposta = requests.get(url)
    dicionario = []
    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.content, "html.parser")
        elemento_p = soup.find("p", class_="significado")
        spans = elemento_p.find_all("span")
        i = 0
        for span in spans:
            span_text = span.text.strip()
            if span_text[-1] != ']':
                if span_text[0].islower():
                    dicionario.append(f'({span_text})')
                else:
                    i += 1
                    dicionario.append(f'{i}. {span_text}')
    return dicionario


#DOIDEIRAS
def remover_acentos_manual(palavra):
    # Mapeia caracteres acentuados para não acentuados
    mapa_acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'ã': 'a', 'õ': 'o',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'ç': 'c',
    }
    palavra_sem_acentos = ''.join(mapa_acentos.get(char, char) for char in palavra)
    return palavra_sem_acentos

    

def traduzir_com_linguee(word):  # limitado, mas tem  --> traduzir_com_linguee
    url = f"https://dictionary.cambridge.org/pt/dicionario/ingles-portugues/{word}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verifica se houve um erro HTTP na resposta

        soup = BeautifulSoup(response.text, 'html.parser')
        elemento_traducao = soup.find(class_='trans dtrans dtrans-se')

        if elemento_traducao:
            traducao = elemento_traducao.get_text(strip=True)
            return traducao.split(',')[0]
        else:
            return f"Palavra não encontrado."
    except requests.exceptions.RequestException as err:
        return f"Erro durante a requisição: {str(err)}"
    
def API_audio(word):
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
    response = requests.get(url + word)
    raudio = -1
    if response.status_code == 200:
        api_dados = response.json()
        dado = api_dados[0]
        for phonetics in dado['phonetics']:
            if (phonetics['audio'] == ''):
                pass
            raudio = phonetics['audio']
    return raudio
