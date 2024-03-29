def calcular_promedio(numeros):

  numeros.sort()
  mediana = (numeros[len(numeros) // 2] + numeros[len(numeros) // 2 - 1]) / 2
  return mediana

def calcular_mediana(numeros):

  numeros.sort()
  mediana = (numeros[len(numeros) // 2] + numeros[len(numeros) // 2 - 1]) / 2
  return mediana

def calcular_promedio_multiplicativo(numeros):
  
  producto = 1
  for numero in numeros:
    producto *= numero
  promedio_multiplicativo = producto ** (1 / len(numeros))
  return promedio_multiplicativo

def ordenar_ascendente(numeros):
  
  numeros.sort()
  return numeros

def ordenar_descendente(numeros):
  
  numeros.sort(reverse=True)
  return numeros

def calcular_potencia(mayor, menor):
  
  potencia = mayor ** menor
  return potencia

def calcular_raiz_cubica(menor):
 
  raiz_cubica = menor ** (1 / 3)
  return raiz_cubica
