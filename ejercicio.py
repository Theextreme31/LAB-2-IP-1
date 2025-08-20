divi = {"Sol": "S/.", "Dolar": "$","Bitcoin": "₿"}
moneda = input("Ingrese el nombre de una divisa (Sol, Dolar, Bitcoin): ") 
if moneda in divi:
    print(f"El símbolo de {moneda} es: {divi[moneda]}")
else:
    print("Esa divisa no está en el diccionario.")