from typing import Counter


my_list_empty = []
print('\nMinha lista vazia é: ',my_list_empty)

my_list_numbers = [1, 2, 3]
print('\nO segundo numero da lista é: ',my_list_numbers[1])

my_list_names = ['Joana', 'Joao', 'Janaina', 'Marcos' ]
print('\nO ultimo nome da lista é: ',my_list_names[-1])

my_list_names_insert = ['Joana', 'Joao', 'Janaina', 'Marcos' ]
last_name = ('Gabriel')

my_list_names_insert.append(last_name)
print('\nFoi Adicionado o nome Gabriel no final da lista: ',my_list_names_insert)

my_list_names_insert.insert(1, 'Renan')
print('\nFoi adicionado o nome renam na segunda posição da lista: ',my_list_names_insert)

my_list_names_insert.remove('Gabriel')
print('\nO nome Gabriel foi removido da lista:', my_list_names_insert)

names = my_list_names_insert
print('\nFoi adicionado o ola em todas posiçoes da lista: \n')
for names in my_list_names_insert:
    print('olá', names)
    print('\nEssa é a lista atual: ',my_list_names_insert)

my_list_names_insert.pop(-1)
print('\nFoi removido o ultimo nome da lista: ',my_list_names_insert)

number_int_list = [6, 22, 26,34]
for number_int in number_int_list:
    convert_number_int = float(number_int)
    print('O numero inteiro antes da conversao é: ',number_int_list)
    print('O numero apos a conversao é: ',convert_number_int)

my_name_tuple = ('Sara', 'Brito')
print('\nMeu nome é: ', my_name_tuple[1], ',', my_name_tuple[0], my_name_tuple[1])


my_name = ['sara', 'brito']

for name in my_name:
    
    print('\nAgora vamos deixar o nome com a primeira letra maiuscula: ', name.capitalize())

list_str_and_int = [2, 'Arroz', 4, 'Feijão',6, 'Macarrão']

print('\nprintando somente os numeros inteiros: ')
print(list_str_and_int[0])
print(list_str_and_int[2])
print(list_str_and_int[4])

Warning_list= ['Perigo cuidado com a escada', 'Cuidado Cao bravo','Perigo Radiação', ' Atencao travessia de pedestre']

for warning in Warning_list:

    if warning.startswith('Perigo') :

        print('\n Essa é a frase com perigo da lista warning: ', warning)


sum_list = [10.5, 15.0, 1.5]
Counter = 0

for numbers in sum_list:

    Counter = Counter + numbers
    
    print ('\nEssa é a soma dos numeros float: ', Counter)


    average_floats = [10.5, 15.0, 1.5]
    amount = len(average_floats) 
    Counter = 0

for numbers_sin in average_floats:

    Counter = Counter + numbers_sin

    average = Counter / amount
    
    print ('\nEssa é a media da lista de numero float: ', average)
