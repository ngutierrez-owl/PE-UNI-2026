#1. Argumentos posicionales
def presentar(nombre, edad):
    print(f"{nombre} tiene {edad} años")
presentar(20, "ana")

# 2. Argumentos por nombre (keyword arguments)
presentar(edad=20, nombre="Ana")
#--------------------------------------------
# 3. Parámetros con valor por defecto
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}")
    #saludar("Luis")

saludar("Luis", "Buenos días")