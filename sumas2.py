

from functools import lru_cache
from os import lseek
from sqlite3.dbapi2 import Cursor
from opBaseDatos import *
from NumerosPrimitiva import *
import operator

def cuentaSumas():  # HACE CONTEO DE LA SUMAS Y LAS DEVUELVE EN UN DICCIONARIO.

    listaSumas = []
    diccionarioSumas = {}
    listaSumas = extraeSumas()
    # Mediante el diccionario almacenamos el la suma y las veces que apaerece en la lista mediante un bucle
    # que genera los valores desde 21-279 min-max valor de la suma de la primitiva.
    for x in range(21,280):
        cuentaApariciones = listaSumas.count(x)
        diccionarioSumas.update({x:cuentaApariciones}) 
    return diccionarioSumas

    #Recorre todos los sorteos y al amancena la suma de cada combinacion en listaSumas.
def extraeSumas():

    listaSumas = []
    combinaciones = leeSorteos() # La funcion retorna todos los sorteos a la lista.
     
    # Recorremos todos los sorteos realizando la suma y los almacenamos en la lista.
    for combinacion in combinaciones:
        numeros = NumerosPrimitiva(combinacion)
        listaSumas.append(numeros.suma())

    return listaSumas

def almacenaCoteoSumas(dicSumas):

    conexion = sqlite3.connect("PRIMITIVA.db")
    cursor = conexion.cursor()
    for x in range (21,280):
        cursor.execute("INSERT INTO tSumas (suma,contador) VALUES (?,?)",(x,dicSumas.get(x)))
        conexion.commit()

    cursor.close()
    conexion.close()

def sumaMedia(lista):
    numeros = []  # Cualquier clase de lista de numeros
    numeros = lista
    contador = 0
    for numero in numeros:
        contador = contador + numero
    media = contador / (len(numeros))
    print (f"La media es {media}")

def listaFrecuencias(lista):
    dFrecuenciasSumas = {}
    lAcumuladorSaltos = []
    contador = 0 
    for x in range(21,280):
        contador = 0
        for suma in lista:
            #print(f"{suma} -> {x}")
            if (x == suma):
                lAcumuladorSaltos.append(contador)
                contador = 0
            else:
                contador = contador + 1
        #print(f"GRABA {x}  --->  {lAcumuladorSaltos}")
        lAcumuladorSaltos.append(contador)
        dFrecuenciasSumas[x] = lAcumuladorSaltos
        print(dFrecuenciasSumas.items())
        print(f"{x} ------> {dFrecuenciasSumas.get(x)}")
        lAcumuladorSaltos.clear()
    
    return dFrecuenciasSumas


          
"""
dSumas = {}
dSumas = cuentaSumas()
SumasOrdenadas = sorted(dSumas.items(), key = operator.itemgetter(1), reverse = True)
"""
listaSumas = []
listaSumas = extraeSumas()
resultado = {}
resultado =listaFrecuencias(listaSumas)
print(resultado.items())
