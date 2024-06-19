
        
        df1.columns = df1.columns.str.lower()
        
        # ### 1.5 Limpar inconsistências nos dados
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
        
        # #### 1.7.1 Alterar tipo de dados
        
        # Lista das colunas que serão convertidas
        colunas_float_e_int = df1.select_dtypes(include = ['number']).columns
        
        # Convertendo as colunas float64 para int64
        df1[colunas_float_e_int] = df1[colunas_float_e_int].astype('int8')
        
        # # 2. (Limpeza dos dados) Passo 2: Engenharia de variáveis
        
        # Convertendo o tipo de idade (em dias e meses) para anos
        df2['idade_anos'] = df2.apply(lambda row: row['nu_idade_n'] / 365 if row['tp_idade'] == 1 else 
                                                  row['nu_idade_n'] * 12 if row['tp_idade'] == 2 else 
                                                  row['nu_idade_n'], axis = 1)
        
        # Eliminando as colunas que foram derivadas
        df2 = df2.drop(columns = ['nu_idade_n', 'tp_idade'], axis = 1)
        
        # * Ajustando os rótulos da variável resposta para sejam aceitas no algoritmo xgboost
        
        # Criando um mapeamento de valores antigos para novos valores da variável resposta
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
        df3 = df3.drop(columns = ['amostra', 'fator_risc'])
        
        # # 5. (Modelagem dos dados) Passo 5: Preparação dos dados
        
        df5 = df4.drop(['id_municip'], axis = 1).copy()
        
        colunas_selecionadas = ['idade_anos', 'tomo_res', 'sg_uf_not',
                                'raiox_res', 'cs_escol_n', 'suport_ven',
                                'cs_raca', 'vacina_cov', 'antiviral', 'asma', 
                                'dose_2_cov', 'dose_ref', 'tp_antivir',
                                'vacina', 'dose_1_cov', 'tp_amostra']
        