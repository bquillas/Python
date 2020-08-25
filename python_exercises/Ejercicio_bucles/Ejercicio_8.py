#[ejercicio 8] Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# https://aprendeconalf.es/python/ejercicios/bucles.html
def my_sol(num):
    print("My solution")
    impares = []
    for i in range(num+1):
        if i % 2 != 0:
            impares.insert(0,str(i))
            print(' '.join(impares))


def other_sol(num):
    print("Other solution")
    for i in range(1,num+1,2):
        for j in range(i,0,-2):
            print(j,end=" ")
        print("")


def run():
    num = int(input("Escribe un numero: "))
    my_sol(num)
    other_sol(num)


if __name__ == "__main__":
    run()