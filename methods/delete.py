from dotenv import load_dotenv
import requests

load_dotenv()

#Deleta algum dado do banco de dados
#Requer algun identificador para saber que sera atualizado
# requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#Dado que sera inserido no banco de dados obs: id e criado automaticamente

url_delete = input("digite a url para ser deletada: ")

requisicao = requests.delete(url_delete)

#mostra o status da requisiçao
print(requisicao)

#mostra o conteudo da requisiçao no caso não tera dados pois foi deletado
print(requisicao.json())