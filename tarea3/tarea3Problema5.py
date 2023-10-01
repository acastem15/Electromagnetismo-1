import numpy as np 
import matplotlib.pyplot as plt
def cuadradoTeorico(matriz): 
    h = 0.1
    i = 100-10

    for j in range(0,len(matriz[0])):

        #print(i*h)
        x = 0 
        y=0
        x_y_1= 0 

  

        for i in range (0,len(matriz[0])): 
            for j in range(0,len(matriz[0])):
                for n in range(0,100):
                    #print(i*h)

                    x = np.sin((((n)*np.pi)/(10))*(i*h))
                    #print(x)
                    alpha_up = (20)*(1-(-1)**n)
                    #print(alpha_up)
                    if alpha_up !=0: 
                        alpha = (alpha_up)/((n)*(np.pi)*np.sinh((n)*np.pi))
                        #print(alpha)
                        x_y = (np.sin(((n)*np.pi/(10))*(i*h)))*(np.sinh(((n)*np.pi/(10))*(j*h)))
                        matriz[i][j]+=alpha*x_y
                        #print(x_y)
        return matriz

    


nuevoTeo =  np.zeros((100,100)) 
teorico = cuadradoTeorico(nuevoTeo).transpose()
plt.imshow(teorico, cmap='jet',interpolation='nearest',origin="lower")
plt.show()

def encontrarCuadrado(nuevo): 
    n = len(nuevo[0])

    for x in range(1, (n//2) ):
        #El x es un delta para ir achiando el cuadrado
        for i in range(x, n-x):
            #cuadrado más pequeño
            #Linea superior
            nuevo[x][i] = (nuevo[x][i-1] + nuevo[x][i+1] + nuevo[x-1][i] + nuevo[x+1][i])/4
            #Linea lateral izquierda
            nuevo[i][x] = (nuevo[i-1][x] + nuevo[i+1][x] + nuevo[i][x-1] + nuevo[i][x+1])/4
            #Linea abajo
            nuevo[n-x-1][i] = (nuevo[n-x-1][i-1] + nuevo[n-x-1][i+1] + nuevo[n-x][i] + nuevo[n-x-2][i])/4
            #Linea lateral derecha
            nuevo[i][n-x-1] = (nuevo[i-1][n-x-1] + nuevo[i+1][n-x-1] + nuevo[i][n-x] + nuevo[i][n-x-2])/4

    return nuevo





def iterarSensitividad(nuevo,viejo,sensitivity): 


    nuevo = encontrarCuadrado(nuevo)

    #print(newCalculated)
    delta =np.abs(np.subtract(nuevo,viejo))

    delta = delta.mean()
 
    print(delta)

    if delta<=sensitivity: 

        plt.imshow(nuevo, cmap='jet',interpolation='nearest')
        plt.show()

        diferencia = nuevo-teorico
        plt.imshow(diferencia, cmap='jet',interpolation='nearest',origin="lower")
        plt.show()

        print(nuevo[0],teorico[0])

        valorDiferencia= 0 
        for i in range(0,len(nuevo[0])):
            for j in range(0,len(nuevo[0])):
                if teorico[i][j]!=0: 
                    valorDiferencia += (nuevo[i][j]-teorico[i][j])/teorico[i][j]

        valordiferencia =valorDiferencia/ len(nuevo[1])**2
        print(valordiferencia)



        return nuevo
    else: 
        viejo = nuevo.copy()
        iterarSensitividad(nuevo,viejo,sensitivity)



viejo = np.zeros ((100,100))

nuevo = np.zeros((100,100)) 

viejo [0] = 5 * np.ones((100))

nuevo[0] = 5*np.ones((100)) 


#print(encontrarCuadrado(nuevo))
potential = iterarSensitividad(nuevo,viejo,0.001)





