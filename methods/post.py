from dotenv import load_dotenv
import requests
import os

load_dotenv()

#Coloca informações inseri no database cria
#Requer envio de dados
# requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#Dado que sera inserido no banco de dados obs: id e criado automaticamente
info = '{"nome":"Matheus"}'

URL_DB_ONE = str(os.getenv("URL_DB_ONE"))

requisicao = requests.post(URL_DB_ONE, data=info)

#mostra o status da requisiçao
print(requisicao)

#mostra o conteudo da requisiçao
print(requisicao.json())