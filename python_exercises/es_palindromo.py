def es_palindromo(palabra):
    reves = palabra[::-1]
    # print(reves)
    if palabra == reves:
        print('Es palindromo!')
    else:
        print('no es palindromo')


def es_palindromo2(palabra):
    lista = []

    for letra in palabra:
        lista.insert(0,letra)
    
    reves = "".join(lista)

    if palabra == reves:
        print('Es palindromo!')
    else:
        print('No es palindromo')



def run():
    palabra = input('Ingrese una palabra: ')
    palabra = palabra.strip()
    palabra = palabra.replace(' ','')
    print(palabra)
    es_palindromo(palabra)
    es_palindromo2(palabra)



if __name__ == "__main__":
    run()