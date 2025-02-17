print("**********************")
print("CALCULADORA BASICA")

num1 = 15
num2 = 3

def suma(num1, num2):
    resultado = num1 + num2
    return resultado

def resta(num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicacion(num1, num2):
    resultado = num1 * num2
    return resultado

def division(num1, num2):
    resultado = num1/num2
    return resultado

print("Suma: ", suma(num1, num2))
print("Resta: ", resta(num1, num2))
print("Multiplicacion: ", multiplicacion(num1, num2))
print("Division: ", division(num1, num2))