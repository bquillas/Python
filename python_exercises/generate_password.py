import random

def generate_password(cant_caracteres):

    numeros = ['1','2','3']
    # numeros.append(cant_caracteres)
    mayuscula = ['A','B','C']

    lista = numeros + mayuscula

    password = []

    for i in range(cant_caracteres):
        caracter_random = random.choice(lista)
        password.append(caracter_random)
    password = ''.join(password)
    return password

    # print(lista)
    # password = []
    # i = 0
    # while i < cant_caracteres:
    #     for caracter in lista:
    #         print(caracter)
    #         password.append(caracter)
    #     i += 1
    # return numeros
    
def run():
    cant_caracteres = int(input("""
    G E N E R A D O R  D E  P A S S W O R D

    De cuantos caracteres desea?: """))

    result = generate_password(cant_caracteres)

    print(result)


if __name__ == '__main__':
    run()