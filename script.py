import os
import pickle
import pandas as pd

class Projeto:
    def __init__(self):
        # Carregando em memória as transformações
        # Obs.: Este é o endereço local do arquivo (endereço absoluto)
        # self.home_path = '/home/leonardo/projetos_/formulario_medico/transformacoes/'
        # Obs.: Este é o endereço na nuvem do arquivo (endereço relativo)
        self.home_path = 'transformacoes/'
        
        self.cs_gestant_scaler = pickle.load(open(self.home_path + 'cs_gestant_scaler.pkl', 'rb'))
        self.cs_raca_scaler = pickle.load(open(self.home_path + 'cs_raca_scaler.pkl', 'rb'))
        self.cs_escol_n_scaler = pickle.load(open(self.home_path + 'cs_escol_n_scaler.pkl', 'rb'))
        self.cs_zona_scaler = pickle.load(open(self.home_path + 'cs_zona_scaler.pkl', 'rb'))
        self.nosocomial_scaler = pickle.load(open(self.home_path + 'nosocomial_scaler.pkl', 'rb'))
        self.ave_suino_scaler = pickle.load(open(self.home_path + 'ave_suino_scaler.pkl', 'rb'))
        self.febre_scaler = pickle.load(open(self.home_path + 'febre_scaler.pkl', 'rb'))
        self.tosse_scaler = pickle.load(open(self.home_path + 'tosse_scaler.pkl', 'rb'))
        self.garganta_scaler = pickle.load(open(self.home_path + 'garganta_scaler.pkl', 'rb'))
        self.dispneia_scaler = pickle.load(open(self.home_path + 'dispneia_scaler.pkl', 'rb'))
        self.desc_resp_scaler = pickle.load(open(self.home_path + 'desc_resp_scaler.pkl', 'rb'))
        self.saturacao_scaler = pickle.load(open(self.home_path + 'saturacao_scaler.pkl', 'rb'))
        self.diarreia_scaler = pickle.load(open(self.home_path + 'diarreia_scaler.pkl', 'rb'))
        self.vomito_scaler = pickle.load(open(self.home_path + 'vomito_scaler.pkl', 'rb'))
        self.puerpera_scaler = pickle.load(open(self.home_path + 'puerpera_scaler.pkl', 'rb'))
        self.cardiopati_scaler = pickle.load(open(self.home_path + 'cardiopati_scaler.pkl', 'rb'))
        self.hematologi_scaler = pickle.load(open(self.home_path + 'hematologi_scaler.pkl', 'rb'))
        self.sind_down_scaler = pickle.load(open(self.home_path + 'sind_down_scaler.pkl', 'rb'))
        self.hepatica_scaler = pickle.load(open(self.home_path + 'hepatica_scaler.pkl', 'rb'))
        self.asma_scaler = pickle.load(open(self.home_path + 'asma_scaler.pkl', 'rb'))
        self.diabetes_scaler = pickle.load(open(self.home_path + 'diabetes_scaler.pkl', 'rb'))
        self.neurologic_scaler = pickle.load(open(self.home_path + 'neurologic_scaler.pkl', 'rb'))        
        self.pneumopati_scaler = pickle.load(open(self.home_path + 'pneumopati_scaler.pkl', 'rb'))
        self.imunodepre_scaler = pickle.load(open(self.home_path + 'imunodepre_scaler.pkl', 'rb'))
        self.renal_scaler = pickle.load(open(self.home_path + 'renal_scaler.pkl', 'rb'))
        self.obesidade_scaler = pickle.load(open(self.home_path + 'obesidade_scaler.pkl', 'rb'))
        self.vacina_scaler = pickle.load(open(self.home_path + 'vacina_scaler.pkl', 'rb'))
        self.antiviral_scaler = pickle.load(open(self.home_path + 'antiviral_scaler.pkl', 'rb'))
        self.tp_antivir_scaler = pickle.load(open(self.home_path + 'tp_antivir_scaler.pkl', 'rb'))
        self.hospital_scaler = pickle.load(open(self.home_path + 'hospital_scaler.pkl', 'rb'))
        self.uti_scaler = pickle.load(open(self.home_path + 'uti_scaler.pkl', 'rb'))
        self.suport_ven_scaler = pickle.load(open(self.home_path + 'suport_ven_scaler.pkl', 'rb'))
        self.raiox_res_scaler = pickle.load(open(self.home_path + 'raiox_res_scaler.pkl', 'rb'))
        self.tp_amostra_scaler = pickle.load(open(self.home_path + 'tp_amostra_scaler.pkl', 'rb'))        
        self.dor_abd_scaler = pickle.load(open(self.home_path + 'dor_abd_scaler.pkl', 'rb'))
        self.fadiga_scaler = pickle.load(open(self.home_path + 'fadiga_scaler.pkl', 'rb'))
        self.perd_olft_scaler = pickle.load(open(self.home_path + 'perd_olft_scaler.pkl', 'rb'))
        self.perd_pala_scaler = pickle.load(open(self.home_path + 'perd_pala_scaler.pkl', 'rb'))
        self.tomo_res_scaler = pickle.load(open(self.home_path + 'tomo_res_scaler.pkl', 'rb'))
        self.vacina_cov_scaler = pickle.load(open(self.home_path + 'vacina_cov_scaler.pkl', 'rb'))
        self.dose_1_cov_scaler = pickle.load(open(self.home_path + 'dose_1_cov_scaler.pkl', 'rb'))
        self.dose_2_cov_scaler = pickle.load(open(self.home_path + 'dose_2_cov_scaler.pkl', 'rb'))
        self.dose_ref_scaler = pickle.load(open(self.home_path + 'dose_ref_scaler.pkl', 'rb'))
        self.idade_anos_scaler = pickle.load(open(self.home_path + 'idade_anos_scaler.pkl', 'rb'))
        
        # Carregando em memória os encoders
        self.sg_uf_not_encoder = pickle.load(open(self.home_path + 'sg_uf_not_encoder.pkl', 'rb'))
        self.cs_sexo_encoder = pickle.load(open(self.home_path + 'cs_sexo_encoder.pkl', 'rb'))

    def limpeza_dos_dados(self, df1):
        # Convertendo em minúsculas
        df1.columns = df1.columns.str.lower()

        # Limpando inconsistências nos dados
        df1 = df1[df1['cs_sexo'].isin(['M', 'F'])]
        df1 = df1[df1['cs_gestant'].isin([1, 2, 3, 4, 5, 6, 9])]
        df1.loc[df1['cs_sexo'] == 'M', 'cs_gestant'] = 6
        df1 = df1[df1['ave_suino'].isin([1, 2, 9])]
        df1 = df1[df1['puerpera'].isin([1, 2, 9])]
        df1.loc[df1['tp_antivir'] == 9, 'tp_antivir'] = 3
        df1.loc[df1['hospital'] == 3, 'hospital'] = 9
        df1.loc[df1['uti'] == 3, 'uti'] = 9
        df1 = df1[df1['amostra'].isin([1, 2, 9])]
        df1 = df1[df1['tp_amostra'].isin([1, 2, 3, 4, 5, 9])]
        df1 = df1[df1['classi_fin'].isin([1, 2, 3, 4, 5])]
        df1 = df1[df1['dose_1_cov'].isin([0, 1])]
        df1 = df1[df1['dose_ref'].isin([0, 1])]
        
        # Inserindo 9 - Não aplicável nas linhas com NaN
        colunas_a_preencher = ['cs_escol_n', 'cs_zona', 'nosocomial', 'febre', 'tosse', 'garganta',
                               'dispneia', 'desc_resp', 'saturacao', 'diarreia', 'vomito', 'dor_abd',
                               'fadiga', 'perd_olft', 'perd_pala', 'cardiopati', 'hematologi', 'sind_down',
                               'hepatica', 'asma', 'diabetes', 'neurologic', 'pneumopati', 'imunodepre',
                               'renal', 'obesidade', 'vacina', 'antiviral', 'hospital', 'uti', 'suport_ven',
                               'raiox_res', 'tomo_res', 'vacina_cov', 'dose_2_cov']
        
        # Criando um dicionário com o valor 9 para todas as colunas
        valores_a_preencher = {coluna: 9 for coluna in colunas_a_preencher}
        
        # Preenchendo os valores nulos
        df1 = df1.fillna(valores_a_preencher)

        # Se a variável 'tp_antivir' é NaN e a variável 'antiviral' é 1, então 'tp_antivir' é definida como 3
        df1['tp_antivir'] = df1.apply(lambda x: 3 if pd.isna(x['tp_antivir']) and x['antiviral'] == 1 else x['tp_antivir'], axis = 1)
        
        # Devido à alta incidência de valores ausentes (NaN) na variável 'tp_antivir', foi decidido atribuir o valor de 0 (zero) sempre que a variável 'antiviral'
        # estiver marcada como 2 ou 9. Essa abordagem foi escolhida para preencher os dados faltantes e garantir a integridade do conjunto de dados
        df1['tp_antivir'] = df1.apply(lambda x: 0 if pd.isna(x['tp_antivir']) and (x['antiviral'] == 2 or x['antiviral'] == 9) else x['tp_antivir'], axis = 1)  
        return df1

    def engenharia_de_variaveis(self, df2):
       # Convertendo o tipo de idade (em dias e meses) para anos
        df2['idade_anos'] = df2.apply(lambda row: row['nu_idade_n'] / 365 if row['tp_idade'] == 1 else 
                                                  row['nu_idade_n'] * 12 if row['tp_idade'] == 2 else 
                                                  row['nu_idade_n'], axis = 1)
        
        # Eliminando as colunas que foram derivadas
        df2 = df2.drop(columns = ['nu_idade_n', 'tp_idade'], axis = 1)
        
        # Ajustando os rótulos da variável resposta para sejam aceitas no algoritmo xgboost        
        # Criando um mapeamento de valores antigos para novos valores davariável resposta
        mapeamento = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
        df2['classi_fin'] = df2['classi_fin'].map(mapeamento)
        
        # Lista original de colunas
        nome_colunas = ['sg_uf_not', 'id_municip', 'cs_sexo', 'cs_gestant', 'cs_raca',
                        'cs_escol_n', 'cs_zona', 'nosocomial', 'ave_suino', 'febre', 'tosse',
                        'garganta', 'dispneia', 'desc_resp', 'saturacao', 'diarreia', 'vomito',
                        'puerpera', 'fator_risc', 'cardiopati', 'hematologi', 'sind_down',
                        'hepatica', 'asma', 'diabetes', 'neurologic', 'pneumopati',
                        'imunodepre', 'renal', 'obesidade', 'vacina', 'antiviral', 'tp_antivir',
                        'hospital', 'uti', 'suport_ven', 'raiox_res', 'amostra', 'tp_amostra',
                        'classi_fin', 'dor_abd', 'fadiga', 'perd_olft', 'perd_pala', 'tomo_res',
                        'vacina_cov', 'dose_1_cov', 'dose_2_cov', 'dose_ref', 'idade_anos']
        
        # Removendo 'classi_fin' da lista
        nome_colunas.remove('classi_fin')
        
        # Adicionando 'classi_fin' ao final da lista
        nome_colunas.append('classi_fin')
        
        # Reorganizando as colunas do DataFrame
        df2 = df2.reindex(columns = nome_colunas)
 
        # Como a variância das colunas 'amostra' e 'fator_risc' são iguais a zero, estas variáveis serão excluidas
        df2 = df2.drop(columns = ['amostra', 'fator_risc', 'id_municip'], axis = 1)
        return df2
        
    def transformacao_dos_dados(self, df5):
        # Aplicando MinMaxScaler
        df5['cs_gestant'] = self.cs_gestant_scaler.fit_transform(df5[['cs_gestant']].values)
        df5['cs_raca'] = self.cs_raca_scaler.fit_transform(df5[['cs_raca']].values)
        df5['cs_escol_n'] = self.cs_escol_n_scaler.fit_transform(df5[['cs_escol_n']].values)
        df5['cs_zona'] = self.cs_zona_scaler.fit_transform(df5[['cs_zona']].values)
        df5['nosocomial'] = self.nosocomial_scaler.fit_transform(df5[['nosocomial']].values)
        df5['ave_suino'] = self.ave_suino_scaler.fit_transform(df5[['ave_suino']].values)
        df5['febre'] = self.febre_scaler.fit_transform(df5[['febre']].values)
        df5['tosse'] = self.tosse_scaler.fit_transform(df5[['tosse']].values)
        df5['garganta'] = self.garganta_scaler.fit_transform(df5[['garganta']].values)
        df5['dispneia'] = self.dispneia_scaler.fit_transform(df5[['dispneia']].values)
        df5['desc_resp'] = self.desc_resp_scaler.fit_transform(df5[['desc_resp']].values)
        df5['saturacao'] = self.saturacao_scaler.fit_transform(df5[['saturacao']].values)
        df5['diarreia'] = self.diarreia_scaler.fit_transform(df5[['diarreia']].values)
        df5['vomito'] = self.vomito_scaler.fit_transform(df5[['vomito']].values)
        df5['puerpera'] = self.puerpera_scaler.fit_transform(df5[['puerpera']].values)
        df5['cardiopati'] = self.cardiopati_scaler.fit_transform(df5[['cardiopati']].values)
        df5['hematologi'] = self.hematologi_scaler.fit_transform(df5[['hematologi']].values)
        df5['sind_down'] = self.sind_down_scaler.fit_transform(df5[['sind_down']].values)
        df5['hepatica'] = self.hepatica_scaler.fit_transform(df5[['hepatica']].values)
        df5['asma'] = self.asma_scaler.fit_transform(df5[['asma']].values)
        df5['diabetes'] = self.diabetes_scaler.fit_transform(df5[['diabetes']].values)
        df5['neurologic'] = self.neurologic_scaler.fit_transform(df5[['neurologic']].values)
        df5['pneumopati'] = self.pneumopati_scaler.fit_transform(df5[['pneumopati']].values)
        df5['imunodepre'] = self.imunodepre_scaler.fit_transform(df5[['imunodepre']].values)
        df5['renal'] = self.renal_scaler.fit_transform(df5[['renal']].values)
        df5['obesidade'] = self.obesidade_scaler.fit_transform(df5[['obesidade']].values)
        df5['vacina'] = self.vacina_scaler.fit_transform(df5[['vacina']].values)
        df5['antiviral'] = self.antiviral_scaler.fit_transform(df5[['antiviral']].values)
        df5['tp_antivir'] = self.tp_antivir_scaler.fit_transform(df5[['tp_antivir']].values)
        df5['hospital'] = self.hospital_scaler.fit_transform(df5[['hospital']].values)
        df5['uti'] = self.uti_scaler.fit_transform(df5[['uti']].values)
        df5['suport_ven'] = self.suport_ven_scaler.fit_transform(df5[['suport_ven']].values)
        df5['raiox_res'] = self.raiox_res_scaler.fit_transform(df5[['raiox_res']].values)
        df5['tp_amostra'] = self.tp_amostra_scaler.fit_transform(df5[['tp_amostra']].values)
        df5['dor_abd'] = self.dor_abd_scaler.fit_transform(df5[['dor_abd']].values)
        df5['fadiga'] = self.fadiga_scaler.fit_transform(df5[['fadiga']].values)
        df5['perd_olft'] = self.perd_olft_scaler.fit_transform(df5[['perd_olft']].values)
        df5['perd_pala'] = self.perd_pala_scaler.fit_transform(df5[['perd_pala']].values)
        df5['tomo_res'] = self.tomo_res_scaler.fit_transform(df5[['tomo_res']].values)
        df5['vacina_cov'] = self.vacina_cov_scaler.fit_transform(df5[['vacina_cov']].values)
        df5['dose_1_cov'] = self.dose_1_cov_scaler.fit_transform(df5[['dose_1_cov']].values)
        df5['dose_2_cov'] = self.dose_2_cov_scaler.fit_transform(df5[['dose_2_cov']].values)
        df5['dose_ref'] = self.dose_ref_scaler.fit_transform(df5[['dose_ref']].values)
        df5['idade_anos'] = self.idade_anos_scaler.fit_transform(df5[['idade_anos']].values)

        # Aplicando LabelEncoder
        df5['sg_uf_not'] = self.sg_uf_not_encoder.fit_transform(df5[['sg_uf_not']].values)
        df5['cs_sexo'] = self.cs_sexo_encoder.fit_transform(df5[['cs_sexo']].values)

        colunas_selecionadas = ['idade_anos', 'tomo_res', 'sg_uf_not',
                                'raiox_res', 'cs_escol_n', 'suport_ven',
                                'cs_raca', 'vacina_cov', 'antiviral', 'asma', 
                                'dose_2_cov', 'dose_ref', 'tp_antivir',
                                'vacina', 'dose_1_cov', 'tp_amostra']
        return df5[colunas_selecionadas]

    def get_prediction(self, modelo, dados_originais, dados_teste):
        pred = modelo.predict(dados_teste)
        dados_originais['classificacao'] = pred
        return dados_originais.to_json(orient = 'records', date_format = 'iso')