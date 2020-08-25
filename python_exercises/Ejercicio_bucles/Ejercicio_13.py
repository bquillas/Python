#[ejercicio 13] Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
# https://aprendeconalf.es/python/ejercicios/bucles.html
def my_sol(palabra):
    print("My solution")
    while palabra != 'salir':
        print(palabra)
        palabra = input(" ")
    print("F I N A L!")



def other_sol(palabra):
    print("Other solution")
    while True:
        palabra = input("Escribe algo: ")
        if palabra == 'salir':
            break
        print(palabra)



def run():
    palabra = input("Ingrese una palabra: ")
    my_sol(palabra)
    other_sol(palabra)


if __name__ == "__main__":
    run()