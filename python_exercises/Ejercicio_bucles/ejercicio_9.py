#[ejercicio 9] Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
# https://aprendeconalf.es/python/ejercicios/bucles.htm

def my_sol(password):
    pas = 'contraseña'

    while password != pas:
        password = input("""
        CONTRASEÑA INVALIDA!
        Ingrese la contraseña correcta: """)
    
    print("""
    Contraseña correcta. LISTO!""")
        


def run():
    password = input("¿Cuál es la contraseña?: ")
    my_sol(password)


if __name__ == "__main__":
    run()

