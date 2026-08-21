def intercambiar(a, b):
    a, b = b, a
    # Solo reasigna las etiquetas LOCALES a y b
    print("Dentro:", a, b)

x, y = 1, 2
intercambiar(x, y)
print("Fuera:", x, y)
# Fuera: 1 2 -> ¡NO se intercambiaron!