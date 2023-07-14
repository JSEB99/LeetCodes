# chatgpt solución
def suma_binaria(binario1, binario2):
    # Convierte los números binarios en enteros
    decimal1 = int(binario1, 2)
    decimal2 = int(binario2, 2)

    # Realiza la suma en base decimal
    suma_decimal = decimal1 + decimal2

    # Convierte el resultado decimal en binario
    resultado_binario = bin(suma_decimal)[2:]

    print(resultado_binario)

suma_binaria("1010","1101")