import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from script import Projeto
import os

class TestProjeto(unittest.TestCase):
    @patch('script.pickle.load')
    @patch('script.os.path.join')
    def setUp(self, mock_join, mock_pickle_load):
        # Mock os.path.join para retornar um caminho fictício
        mock_join.side_effect = lambda *args: os.path.join('/dummy/path', args[-1])
        
        # Função para retornar mocks de scaler ou encoder
        def mock_pickle_loader(file):
            mock_scaler = MagicMock()
            mock_scaler.transform = MagicMock(return_value=[0.5])
            return mock_scaler
        
        mock_pickle_load.side_effect = mock_pickle_loader
        
        # Inicializa o objeto Projeto
        self.projeto = Projeto()

    def test_limpeza_dos_dados(self):
        df = pd.DataFrame({
            'cs_sexo': ['M', 'F', 'M'],
            'cs_gestant': [1, 6, 9],
            'ave_suino': [1, 2, 9],
            'puerpera': [1, 2, 9],
            'tp_antivir': [1, 9, None],
            'antiviral': [1, 2, 2],
            'cs_escol_n': [None, 2, 3],
        })
        cleaned_df = self.projeto.limpeza_dos_dados(df)
        self.assertEqual(cleaned_df['cs_gestant'].iloc[0], 1)
        self.assertEqual(cleaned_df['cs_gestant'].iloc[2], 9)
        self.assertEqual(cleaned_df['tp_antivir'].iloc[2], 0)

    def test_engenharia_de_variaveis(self):
        df = pd.DataFrame({
            'nu_idade_n': [365, 2, 30],
            'tp_idade': [1, 2, 3],
            'classi_fin': [1, 2, 3],
        })
        engineered_df = self.projeto.engenharia_de_variaveis(df)
        self.assertEqual(engineered_df['idade_anos'].iloc[0], 1)
        self.assertEqual(engineered_df['idade_anos'].iloc[1], 24)
        self.assertEqual(engineered_df['classi_fin'].iloc[0], 0)

    def test_transformacao_dos_dados(self):
        df = pd.DataFrame({
            'idade_anos': [1, 2, 3],
            'tomo_res': [1, 2, 3],
            'sg_uf_not': ['SP', 'RJ', 'MG'],
            'cs_sexo': ['M', 'F', 'M'],
        })
        transformed_df = self.projeto.transformacao_dos_dados(df)
        self.assertIn('idade_anos', transformed_df.columns)
        self.assertIn('sg_uf_not', transformed_df.columns)
        self.assertEqual(transformed_df['idade_anos'].iloc[0], 0.5)
        self.assertEqual(transformed_df['sg_uf_not'].iloc[0], 1)

    def test_get_prediction(self):
        df_original = pd.DataFrame({'feature1': [1], 'feature2': [2]})
        df_teste = pd.DataFrame({'feature1': [0.5], 'feature2': [0.5]})
        
        mock_model = MagicMock()
        mock_model.predict = MagicMock(return_value=[1])
        
        result = self.projeto.get_prediction(mock_model, df_original, df_teste)
        self.assertIn('classificacao', pd.read_json(result).columns)

if __name__ == '__main__':
    unittest.main()
