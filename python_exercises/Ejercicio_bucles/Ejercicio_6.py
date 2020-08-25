#[Ejercicio 6] Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
def make_triangle(num):
    ast = []
    i = 0
    if num <= 0:
        print('Escribe numero mayores a 0')
    else:
        while i < num:
            ast.append('*')
            print(''.join(ast))
            i += 1


def make_triangle2(num):
    for i in range(num):
        print("*"*(i+1))


def make_triangle3(num):
    for i in range(num):
        for j in range(i+1):
            print('*',end="")
        print("")

def run():
    num = int(input("Altura del triangulo: "))
    make_triangle(num)
    make_triangle2(num)
    make_triangle3(num)



if __name__ == "__main__":
    run()