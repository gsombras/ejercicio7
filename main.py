telefono = list()
nombre = list()
while True:
    entrada = input("Nombre (fin para terminar): ")
    dato = input("Teléfono (fin para terminar): ")
    if entrada != 'fin':
        nombre.append(entrada)
        telefono.append(dato)
    else:
        break

for entrada in nombre:
    print("Nombre: ", entrada)
for dato in telefono:
    print("Teléfono: ", dato)
