#ejercicio1 Usamos recursión con memorización para calcular números de Fibonacci
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    lisa = []
    return memo[n]
# Calcular el número de Fibonacci de 50
resultado = fibonacci(50)

print(resultado)

print("--------------------------------------------")

# ejercicio 2
from decimal import Decimal, getcontext
# Establecemos un contexto de precisión alta
getcontext().prec = 50
# Realizamos una operación matemática precisa
numero1 = Decimal('1.123456789123456789')
numero2 = Decimal('2.987654321987654321')
resultado = numero1 * numero2
# Mostramos el resultado con alta precisión
print(f"Resultado preciso: {resultado}")

print("--------------------------------------------")

#jercicio 3
import re
# Usamos una expresión regular avanzada para extraer palabras en mayúsculas de una cadena
cadena = "ESTO es un EJEMPLO de uso AVANZADO de CADENAS y Expresiones REGULARES."
# Expresión regular que busca palabras completamente en mayúsculas
patron = r'\b[A-Z]{2,}\b'
# Encontramos todas las coincidencias
palabras_mayusculas = re.findall(patron, cadena)
print("Palabras en mayúsculas:", palabras_mayusculas)

print("-------------------------------------------")

# ejercicio4 Verificación de condiciones complejas usando operadores lógicos
a = True
b = False
c = True

# Uso de operadores lógicos avanzados (AND, OR, XOR)
resultado = (a and b) or (a and c) ^ b

print("Resultado de la operación lógica compleja:", resultado)

print("-----------------------------------------------")
# ejercicio 5 Función que combina valores numéricos y maneja valores nulos
def sumar_o_default(a, b):
    # Si uno de los valores es None, retornamos 0 como valor predeterminado
    return (a or 0) + (b or 0)

# Ejemplo con diferentes combinaciones de enteros y valores None
print(sumar_o_default(6, None))  # Debería retornar 5
print(sumar_o_default(None, None))  # Debería retornar 0
print(sumar_o_default(4, 24))  # Debería retornar 28