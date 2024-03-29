from operaciones import *

numeros = []
for i in range(5):
  numero = float(input(f"Introduzca el número {i + 1}: "))
  numeros.append(numero)

promedio = calcular_promedio(numeros)
mediana = calcular_mediana(numeros)
promedio_multiplicativo = calcular_promedio_multiplicativo(numeros)
numeros_ascendentes = ordenar_ascendente(numeros)
numeros_descendentes = ordenar_descendente(numeros)
mayor = numeros_descendentes[0]
menor = numeros_ascendentes[0]
potencia = calcular_potencia(mayor, menor)
raiz_cubica = calcular_raiz_cubica(menor)

print(f"Promedio: {promedio}")
print(f"Mediana: {mediana}")
print(f"Promedio multiplicativo: {promedio_multiplicativo}")
print(f"Números ordenados de forma ascendente: {numeros_ascendentes}")
print(f"Números ordenados de forma descendente: {numeros_descendentes}")
print(f"Potencia del mayor número elevado al menor número: {potencia}")
print(f"Raíz cúbica del menor número: {raiz_cubica}")
