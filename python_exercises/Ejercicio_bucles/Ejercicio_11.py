#[ejercicio 11] Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
# https://aprendeconalf.es/python/ejercicios/bucles.html
def my_sol(palabra):
    print("My solution")
    lista=[]
    for caracter in palabra:
        # print(caracter, end=" ")
        lista.insert(0,caracter)
        
    print(' '.join(lista))


def other_sol(palabra):
    print("Other solution")
    for i in range(len(palabra)-1,-1,-1):
        print(palabra[i])



def run():
    palabra = input("Ingrese una palabra: ")
    my_sol(palabra)
    other_sol(palabra)


if __name__ == "__main__":
    run()