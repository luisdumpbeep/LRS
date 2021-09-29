class NumerosPrimitiva():


    def __init__(self,combinacion):

        self.combinacion = list([combinacion[1], combinacion[2], combinacion[3], combinacion[4], combinacion[5], combinacion[6]])

    def agrupa(self,combinacion):

        self.combinacion = [[combinacion[1], combinacion[2], combinacion[3], combinacion[4], combinacion[5], combinacion[6]]]
        
    def imprimeCombinacion (self):
        print(self.combinacion)

    def generaCuadrigas(self):
        conjuntoCuadrigas = []
        for a in range(0,3):
            for b in range(a+1,4):
                for c in range (b+1,5):
                    for d in range (c+1,6):
                        conjuntoCuadrigas.append([self.combinacion[a], self.combinacion[b], self.combinacion[c],
                        self.combinacion[d]])
        return conjuntoCuadrigas

    def suma(self):
        total = 0
        for numero in self.combinacion:
            total = total + numero
        
        return total
    
    def parImpar(self):

        par = 0
        impar = 0

        for numero in self.combinacion:
            if (numero % 2 == 0):
                par = par + 1
            else:
                impar = impar + 1
    
        return par, impar
    
    def decenas(self):

        tipoDecenas = { 0:0, 1:0, 2:0, 3:0, 4:0}

        for numero in self.combinacion:
            if ((numero > 0) and (numero < 10)):
                valor = tipoDecenas.get(0) + 1
                tipoDecenas = {**tipoDecenas, 0:valor}
            elif ((numero >= 10) and (numero < 20)):
                valor = tipoDecenas.get(1) + 1
                tipoDecenas = {**tipoDecenas, 1:valor}
            elif ((numero >= 20) and (numero < 30)):
                valor = tipoDecenas.get(2) + 1
                tipoDecenas = {**tipoDecenas, 2:valor}
            elif ((numero >= 30) and (numero < 40)):
                valor = tipoDecenas.get(3) + 1
                tipoDecenas = {**tipoDecenas, 3:valor}
            else:
                valor = tipoDecenas.get(4) + 1
                tipoDecenas = {**tipoDecenas, 4:valor} 

        """"
        print (f"10s: {tipoDecenas.get(0)}")
        print (f"20s: {tipoDecenas.get(1)}")
        print (f"30s: {tipoDecenas.get(2)}")
        print (f"40s: {tipoDecenas.get(3)}")
        """
        return tipoDecenas

    def consecutivos (self):

        contador = 0 
        secuencia = []

        for x in range(0,5):

            secuencia.append(self.combinacion[x])
            if (self.combinacion[x+1] == (self.combinacion[x]+1)):
                contador = contador + 1
                secuencia.append(self.combinacion[x+1])
            else:
                if(contador > 0):
                    print(f"{set(secuencia)}   nº consecutivos {contador}")
                    secuencia.clear()
                    contador = 0
                else:
                    contador = 0
                    secuencia.clear()
            
        if(contador > 0):
            print(f"{set(secuencia)}   nº consecutivos {contador}")
    
    

 

