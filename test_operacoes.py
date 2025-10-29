# -*- coding: utf-8 -*-
import unittest

from operacoes_lista import (
    capitalizar_nomes,
    filtrar_inteiros,
    filtrar_warnings_por_prefixo,
    calcular_soma,
    calcular_media
)

class TestOperacoesLista(unittest.TestCase):

    def test_deve_capitalizar_nomes(self):
        lista = ['sara', 'brito']
        esperado = ['Sara', 'Brito']
        self.assertEqual(capitalizar_nomes(lista), esperado)

    def test_deve_filtrar_inteiros(self):
        lista = [2, 'Arroz', 4, 'Feijão', 6, 'Macarrão']
        esperado = [2, 4, 6]
        self.assertEqual(filtrar_inteiros(lista), esperado)

    def test_deve_filtrar_warnings_com_prefixo_perigo(self):
        lista = ['Perigo cuidado com a escada', 'Cuidado Cao bravo', 'Perigo Radiação', ' Atencao travessia']
        esperado = ['Perigo cuidado com a escada', 'Perigo Radiação']
        self.assertEqual(filtrar_warnings_por_prefixo(lista, 'Perigo'), esperado)

    def test_deve_filtrar_warnings_ignorando_espaco_extra(self):
        lista = [' Perigo Radiação'] 
        esperado = [' Perigo Radiação']
        self.assertEqual(filtrar_warnings_por_prefixo(lista, 'Perigo'), esperado)

    def test_deve_calcular_soma(self):
        lista = [10.5, 15.0, 1.5]
        self.assertEqual(calcular_soma(lista), 27.0)

    def test_deve_calcular_media(self):
        lista = [10.5, 15.0, 1.5]
        self.assertEqual(calcular_media(lista), 9.0)

    def test_deve_retornar_media_zero_para_lista_vazia(self):
        lista = []
        self.assertEqual(calcular_media(lista), 0.0)

if __name__ == '__main__':
    unittest.main()
