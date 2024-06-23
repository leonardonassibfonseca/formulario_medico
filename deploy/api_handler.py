import pickle
import os
import pandas as pd
from flask import Flask, request, Response

# Diretório onde está salvo a API handler.py
# Nome do arquivo.py
# Nome da classe que foi criada dentro do arquivo.py

# from Diretório.arquivo        import classe
from script import Projeto

# Carregando o modelo treinado usando pickle
# Obs.: Este é o endereço local do arquivo (endereço absoluto)
modelo = pickle.load(open('/home/leonardo/projetos_/formulario_medico/modelo/modelo_treinado.pkl', 'rb'))
# Obs.: Este é o endereço na nuvem do arquivo (endereço relativo)
# modelo = pickle.load(open('modelo/modelo_treinado.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return 'Servidor Flask está funcionando normalmente!'

@app.route('/predict', methods = ['POST'])
def predict():
    teste_json = request.get_json() # Recebe um arquivo JSON a partir da request

    if teste_json:  # Se o teste_json for diferente de vazio, ou seja, se foi carregado algum dado
        # Verifica se o arquivo passado é um tipo de dicionário e se sim, foi enviado um arquivo com somente uma linha
        if isinstance(teste_json, dict):
            # Cria um dataframe e para isso é necessário indicar no Pandas qual é o nº da linha inicial, nesta caso, 0
            dados_brutos_que_vieram_da_producao = pd.DataFrame(teste_json, index = [0])
        else:
            # Se não for é um dicionário, foi enviado um arquivo com mais de uma linha
            dados_brutos_que_vieram_da_producao = pd.DataFrame(teste_json, columns = teste_json[0].keys())

        # Instanciando a classe do projeto
        pipeline = Projeto()
        
        # Limpeza_dos_dados
        df1 = pipeline.limpeza_dos_dados(dados_brutos_que_vieram_da_producao)
        
        # Engenharia_de_atributos
        df2 = pipeline.engenharia_de_variaveis(df1)

        # Transformação dos dados
        df5 = pipeline.transformacao_dos_dados(df2)
        
        # Predição
        df_resposta = pipeline.get_prediction(modelo, dados_brutos_que_vieram_da_producao, df5)
        
        return df_resposta
    else:
        return Response('{}', status = 200, mimetype = 'application/json')

if __name__ == '__main__':
    # Dizer para endpoint rodar no localhost (rodando na máquina)
    # port = os.environ.get('PORT', 5000)
    # app.run('0.0.0.0', port = port)
    app.run('0.0.0.0', debug = True)
