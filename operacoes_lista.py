# -*- coding: utf-8 -*-

def capitalizar_nomes(lista_de_nomes):
    """Recebe uma lista de nomes e retorna uma nova lista com eles capitalizados."""
    lista_capitalizada = []
    for nome in lista_de_nomes:
        lista_capitalizada.append(nome.capitalize())
    return lista_capitalizada

def filtrar_inteiros(lista_mista):
    """Recebe uma lista mista e retorna uma nova lista apenas com os inteiros."""
    lista_de_inteiros = []
    for item in lista_mista:
        if isinstance(item, int):
            lista_de_inteiros.append(item)
    return lista_de_inteiros

def filtrar_warnings_por_prefixo(lista_de_warnings, prefixo):
    """
    Recebe uma lista de avisos e um prefixo,
    e retorna uma nova lista com os avisos que começam com o prefixo.
    """
    lista_filtrada = []
    for warning in lista_de_warnings:
        if warning.strip().startswith(prefixo):
            lista_filtrada.append(warning)
    return lista_filtrada

def calcular_soma(lista_de_numeros):
    """Recebe uma lista de números e retorna a soma total."""
    soma_total = 0
    for numbers in lista_de_numeros:
        soma_total = soma_total + numbers
    return soma_total

def calcular_media(lista_de_numeros):
    """Recebe uma lista de números e retorna a média."""
    # Teste de Borda: Se a lista for vazia, evitamos um erro de divisão por zero.
    if not lista_de_numeros:
        return 0.0
        
    soma_para_media = calcular_soma(lista_de_numeros)
    media = soma_para_media / len(lista_de_numeros)
    return media
