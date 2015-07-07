 #!/usr/bin/python
# _-_ coding: UTF-8 -*-
import tweepy, os

''' 
Script simple que utiliza el API de Twitter para twittear cada hora 100 decimales de PI.

Los decimales se pueden calcular fácilmente mediante un algoritmo, pero para no reinventar la rueda se ha usado un fichero de texto que 
contiene los primeros 10 millones de decimales. El fichero ha sido generado con el programa PiFast32.

Adicionalmente, se ha usado el cron de Linux para automatizar la tarea y llamar al script cada hora. Se explica con más detalle en el Readme.

Autor: Felipe Arcos González (@Felipe_Ark)
Implementado y funcionando en la cuenta de Twitter @pidecimal

'''

# Autenticación en Twitter
CONSUMER_KEY = 'Rellenar con datos propios'
CONSUMER_SECRET = 'Rellenar con datos propios'
ACCESS_KEY = 'Rellenar con datos propiosD'
ACCESS_SECRET = 'Rellenar con datos propios'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
 
# Apertura del fichero principal en modo solo lectura
fo = open("pi.txt", "r")

# Lectura de las líneas, se guardan en una lista
lineas = fo.readlines()

# Apertura de un nuevo fichero temporal vacío, para su escritura
fo2 = open("pi_bkp.txt","w")

# Recorrido de las líneas del primer fichero
numero_linea = 0
contenido_linea = ''

for line in lineas:
  # Si es la primera línea, se guarda el contenido en una variable
  if numero_linea == 0:
    contenido_linea = line
  # En caso contrario, se escribe cada línea en el fichero temporal
  else:
    fo2.write(line)
  # Al final, se aumenta el contador
  numero_linea = numero_linea + 1
  
# Cierre de los ficheros
fo.close()
fo2.close()

# Se elimina el fichero principal y se renombra el fichero temporal con el nombre del primero
os.remove("pi.txt")
os.rename("pi_bkp.txt", "pi.txt")

# Se calcula el número de decimal que se muestra, utilizando el número que aparece al final de cada línea
# Por ejemplo, la línea 4 contiene los decimales 301 a 400.
final_decimal = int(contenido_linea[-5:])
final_decimal = final_decimal * 100
inicio_decimal = final_decimal - 99

# Se forma la cadena de texto que formará el tweet
cadena_final = str(contenido_linea[:-6]) + "(Decimales " + str(inicio_decimal) + " a " + str(final_decimal) + ")"

# Se usa la API de Twitter para actualizar el estado, twitteando la cadena formada anteriormente. También se imprime por consola
tweepy.API(auth).update_status(status=cadena_final)
print(cadena_final)