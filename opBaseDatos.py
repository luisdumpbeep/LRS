import sqlite3

def leeSorteos():
    conexion = sqlite3.connect("PRIMITIVA.db")
    cursor = conexion.cursor()
    
    instruccion = "SELECT FECHA, B1, B2, B3, B4, B5, B6 FROM tablaSorteos ORDER BY FECHA ASC"

    cursor.execute(instruccion)

    combinaciones = cursor.fetchall()

    cursor.close()
    conexion.close()

    return combinaciones

def aparicionesHistorico(*args):

    
    print(f"Numeros para comprobar: {args}")
    compruebaExistenciaCuadriga(*args)
    conexion = sqlite3.connect('PRIMITIVA.db')
    cursor = conexion.cursor()
    #instruccion = "SELECT fECHA,B1,B2,B3,B4,B5,B6 FROM tablaSorteos WHERE FECHA BETWEEN 20200000 AND 20201231 ORDER BY FECHA ASC"
    instruccion = "SELECT fECHA,B1,B2,B3,B4,B5,B6 FROM tablaSorteos ORDER BY FECHA ASC"
    cursor.execute(instruccion)

    resultado = cursor.fetchall()

    salidas=[] # Almacena los nº sorteos cuando sale la combinacion
    apuntador = 0 # Indica el número de Sorteo en el que estamos.
    cuadriga = set(*args)

    for coincidencias in resultado: 
        compara = set (coincidencias)
        apuntador = apuntador + 1 
        if (len(cuadriga & compara) == len(cuadriga)):
            salidas.append(apuntador)

    totalSorteos = len(resultado)
    numeroSalidas = len(salidas)
    if (numeroSalidas>1):
        vecesSinSalir = apuntador - salidas[-1]
        print (f"Total de sorteos {totalSorteos}   Veces salidas   {numeroSalidas}    Tiempo sin salir  {vecesSinSalir}")
    else:
        print (f"Total de sorteos {totalSorteos}   Veces salidas   {numeroSalidas}")

def grabaCuadrigas(cuadriga):
    conexion = sqlite3.connect('PRIMITIVA.db')
    cursor = conexion.cursor()
    cursor.execute(f"INSERT INTO tablaCuadrigas VALUES (cuadriga[0],cuadriga[1], cuadriga[2],cuadriga[3])")
    conexion.commit()
    cursor.close()
    conexion.close()

def compruebaExistenciaCuadriga(cuadriga):

    conexion = sqlite3.connect('PRIMITIVA.db')
    cursor = conexion.cursor()
    cursor.execute(f"SELECT B1,B2,B3,B4 FROM  tablaCuadrigas WHERE B1={cuadriga[0]} AND B2={cuadriga[1]} AND B3={cuadriga[2]} AND B4={cuadriga[3]}")
    resultados = cursor.fetchall()
    if (len(resultados) > 0):
        print("existe")
    else:
        print("no existe")

    cursor.close()
    conexion.close()
