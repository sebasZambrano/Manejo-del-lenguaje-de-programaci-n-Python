# Solicita al usuario el número de diseños a evaluar
print("Ingrese la cantidad de diseños de ruedas que desea evaluar:")
N = int(input())  # Lee el número N y lo convierte a entero

db = []  # Inicializa la lista donde se almacenarán los registros

print(f"Ingrese los {N} registros, uno por línea con el formato:")
print("DIÁMETRO(mm) GROSOR(mm) ANCHO(mm) PRECIO")

# Solicita los datos de cada diseño y los guarda en db
for i in range(N):
    c = input(f"Ingrese diseño #{i+1}: ")  # Lee una línea de entrada
    db.append(c.split(' '))  # Divide la línea en partes y la guarda como lista

# Parámetros reglamentarios definidos por la organización
P1 = 100   # Diámetro mínimo permitido
P2 = 120   # Diámetro máximo permitido
P3 = 70    # Grosor mínimo permitido
P4 = 80    # Grosor máximo permitido
P5 = 90    # Ancho mínimo permitido
P6 = 110   # Ancho máximo permitido

disponibilidad = False  # Variable para saber si hay diseños válidos
exito = []  # Lista para guardar los precios de los diseños que cumplen el reglamento

# Recorre cada diseño e identifica si cumple el reglamento
for i in range(N):
    diametro = int(db[i][0])  # Extrae el diámetro
    grosor = int(db[i][1])    # Extrae el grosor
    ancho = int(db[i][2])     # Extrae el ancho
    precio = int(db[i][3])    # Extrae el precio

    # Verifica si el diseño cumple todos los parámetros reglamentarios
    if (P1 <= diametro <= P2) and (P3 <= grosor <= P4) and (P5 <= ancho <= P6):
        exito.append(precio)      # Si cumple, agrega el precio a la lista de éxito
        disponibilidad = True     # Indica que al menos uno cumple

# Imprime resultados según si hubo o no diseños válidos
if not disponibilidad:
    print("NO DISPONIBLE")  # Si ningún diseño cumple, lo indica
else:
    print("Precios de diseños que cumplen con el reglamento:")
    for precio in exito:
        print(precio)  # Muestra los precios de los diseños válidos