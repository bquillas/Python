'z' > 'a' #Operador Relacional
#True
"""
    Esto por que esta en una pocisiòn más despues el 'z' que la 'a' 
"""


10 > 15 and 15 > 20 #Operador Lógico
#False
"""
    Para que 'and' nos devuelva un valor verdadero 'True', tiene que ser verdadero ambas condicionales
    Si uno de ellos es Falso, nos devolverà Falso. 
    Ambas condicionales tinen que cumplir la condicion 
"""


'a' == 'a' or 'b' != 'b' #Operador Lógico
#True
""" 
    Solo necesita cumplirse una de las condiciones para que nos de resultado True
    Si ambos son Falso, resultara Falso
"""

def say_helo(age):
    if age > 18:
        print("Hola senior")
    else:
        print("Hola Adolescente")
