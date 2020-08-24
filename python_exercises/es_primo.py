import math

def es_primo(numero):
    #!Falta validar de que el 1 no es primo
    contador = 0
    for i in range(1,numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    
    if contador > 0:
        print("El número {}, NO es primo.".format(numero))
    else:
        print("El número {} es PRIMO!.".format(numero))

def is_prime(numero):
    if(numero < 2):
        return False
    root = math.sqrt(numero)
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True


def run():
    numero = int(input("Ingrese un número: "))
    es_primo(numero)

    if is_prime(numero):
        print("Es Primo!")
    else:
        print("No es Primo")

if __name__ == "__main__":
    run()
