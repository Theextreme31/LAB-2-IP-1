def suma(a, b):
    """Devuelve la suma de a y b"""
    return a + b
def resta(a, b):
    """Devuelve la resta de a menos b"""
    return a - b
def multi(a, b):
    """Devuelve la multiplicación de a por b"""
    return a * b

def divi(a, b):
    """Devuelve la división de a entre b.
       Si b es cero devuelve un mensaje de error.
    """
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"