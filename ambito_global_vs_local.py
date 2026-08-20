contador = 0
def incrementar():
    contador = contador + 1
    print ("Este es el valor de CONTADOR: ",contador)
# ERROR: UnboundLocalError print(contador) incrementar()
# Python no permite leer "contador" porque ya lo considera local