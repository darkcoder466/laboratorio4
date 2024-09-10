# actividad 1
numeros = [1,2,3,4,5,6] # definimos una lista de numeros enteros

cuadrados = [numero **2 for numero in numeros] # usamos una lista por comprension para guardar los numeros al cuadrado

print(f"lista de numeros al cudrado {cuadrados}") #imprimir la lista de numeros al cuadrado

print("-------------------------------------------------------------")

# actividad 2
nombre = "carlos" #se define la variable edad de tipo cadena
edad = 27 # se define la variable edad de tipo entero 
altura = 1.76 # se define la variable altura de tipo float

mensaje = f"mi nombre es {nombre} tengo {edad} años y mido {altura} metros"

print(mensaje) # imprimir el mensaje

print("-------------------------------------------------------------")

# Definimos una variable para la edad
edad = 21

# Usamos un condicional para verificar la mayoría de edad
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

print("-------------------------------------------------------------")

# Definimos una variable de tipo flotante
saldo = 250.0

# Simulamos un ciclo de retiros de saldo hasta que el saldo sea menor que 10
while saldo > 10:
    retiro = 15.0
    saldo -= retiro
    print(f"Se ha retirado {retiro}, saldo actual: {saldo}")

print("-------------------------------------------------------------")

# Definimos un diccionario con información personal
persona = {
    "nombre": "Fabian Andres Rosero",
    "edad": 21,
    "ciudad": "Sevilla"
}
# Iteramos sobre las claves y valores del diccionario
for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")



