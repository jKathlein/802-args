# def item (**param):
#     print(f'{chave} : {valor})
#     for item in *param.itens():
#
# item(nome='Groger', id=1)


def imprimir_qualquer_coisa(*args):
    for numero, item in enumerate(args):
        print(str(numero) + '-> ' + item)

imprimir_qualquer_coisa('Uva', 'Pera', 'Morango')