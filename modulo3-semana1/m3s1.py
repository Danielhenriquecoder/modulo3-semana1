import requests 
import json
# link para API
link=f'https://parallelum.com.br/fipe/api/v1/carros/marcas'

retornar_dados = requests.get(link) #retornando dados da API
if retornar_dados.status_code == 200:
    marcas = retornar_dados.json()#convertendo dados para formato json
else:
    print('ocorreu um erro ao resgatar a API')



#usei 'print(marcas)' para ver e escolher as marcas de carros e selecionar o id

ID = 55 #id selecionado '55'

class Modelo:
    def __init__(self,ID):
        self.id_marca_selecionada = ID #recebe id como parametro
        headers = {
            'user-Agent':'MyApp/1.0'
        }#autenticação API
        self.link_modelos = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{self.id_marca_selecionada}/modelos' #link com parametro inserido

        self.retornar_modelos= requests.get(self.link_modelos, headers = headers) #retornando dados da marca de carro selecionada
        self.modelos_veiculos = self.retornar_modelos.json() #convertendo dados para formato json
        self.dados_modelos = self.modelos_veiculos['modelos']
        self.contador = 0 #inicio da contagem
        self.fim = len(self.dados_modelos) #fim da contagem
        

    def __iter__(self):
        return self

    def __next__(self):
        if self.contador >= self.fim:
            raise StopIteration
        resultado = self.dados_modelos[self.contador] #contador inicia em zero
        self.contador += 1 #conador soma + 1
        return resultado #retornando dado atual
    
Suzuki = Modelo(ID) #criando objeto

for carro in Suzuki: #extraindo dados do  objeto
    nome_carro = carro['nome']
    id_carro = carro['codigo']
    print(f'ID: {id_carro} nome: {nome_carro}')

    