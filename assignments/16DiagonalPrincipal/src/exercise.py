
def main():
    #Se establecen las variables y listas vacias
    diagonal = []
    auxiliar = 0
    r=int(input("")) #Pide número de renglones
    c=int(input("")) #Pide número de columnas

    #Se crea un ciclo para comprobar si es matriz cuadrada o no
    if r != c:    #Cuando el numero de renglones sea diferente al de columnas, mostrara un error
        print("La matriz no es cuadrada")
    else:
        #Se crea otro ciclo para capturar valores para la lista
        for captura in range(0,r*c): 
            valor = int(input("")) 
            if auxiliar == 0:
                diagonal.append(valor)
            auxiliar +=1 
            #El auxiliar funciona como un punto de referencia para conocer la posicion y en la matriz
            if auxiliar == r+1:
                auxiliar = 0
        print(diagonal)
        

if __name__=='__main__':
    main()
