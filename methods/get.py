from dotenv import load_dotenv
import requests
import os

load_dotenv()

#Pega as informaçoes
# requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
URL_DB = str(os.getenv("URL_DB"))
requisicao = requests.get(URL_DB)

#mostra o status da requisiçao
print(requisicao)

#mostra o conteudo da requisiçao
print(requisicao.json())