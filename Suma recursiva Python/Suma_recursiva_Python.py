def suma_recursiva(n):
    if n <= 9:
        return n
    else:
        return suma_recursiva(n // 10) + n % 10

try:
    numero = int(input("Ingresa un n�mero entero: "))
    resultado = suma_recursiva(numero)
    print(f"La suma de los d�gitos de {numero} es: {resultado}")
except ValueError:
    print("Entrada no v�lida. Debes ingresar un n�mero entero.")

