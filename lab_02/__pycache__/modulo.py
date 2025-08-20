__contador = 0
def sumalista(lista):
    global __contador
    __contador += 1
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma
def multiplicalista(lista):
    global __contador
    __contador += 1
    multiplica = 1
    for elemento in lista:
        multiplica *= elemento
    return multiplica
if __name__ == "__main__":
    print("EPIS, tengo preferencia por ser un módulo, haciendo algunas pruebas.")
    mi_lista = [i + 1 for i in range(4)]  # [1,2,3,4]
    print(sumalista(mi_lista) == 10)       # True
    print(multiplicalista(mi_lista) == 24) # True
