#[ejercicio 12] Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
# https://aprendeconalf.es/python/ejercicios/bucles.html
def my_sol(frase,letra):
    print("My solution")
    contador = 0
    for caracter in frase:
        if caracter == letra:
            contador += 1
    print("La letra {}, se repitió {} veces".format(letra,contador))



def other_sol(frase,letra):
    print("Other solution")
    contador = 0
    for i in frase:
        if i == letra:
            contador += 1
    print("La letra '%s' aparece %2i veces en la frase '%s'."%(letra,contador,frase))




def run():
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra a contar: ")
    my_sol(frase,letra)
    other_sol(frase,letra)


if __name__ == "__main__":
    run()