def exchange_soles_dolar(ammount):
    dolar_val = 3.5

    return ammount / dolar_val


def run():

    print("""
    C A L C U L A D O R A  D E  D I V I S A S
    
        Cambio de Nuevos Soles a Dolares

    """)

    ammount = float(input("How much S/. do you want to exchange?: "))

    result = round(exchange_soles_dolar(ammount),2)

    print('S/.{} Nuevos Soles are ${} dólares'.format(ammount,result))




if __name__ == '__main__':
    run()