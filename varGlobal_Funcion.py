import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv("water_potability.csv")

# Visualizar las primeras 5 filas
print(df.head())


saldo = 1000
def retirar_sin_global(monto):
    saldo = saldo - monto
    print("Dentro (local):", saldo)
#--------------------

def retirar_con_global(monto):
    global saldo
    saldo = saldo - monto
    print("Dentro (global):", saldo)
print (retirar_con_global(100))