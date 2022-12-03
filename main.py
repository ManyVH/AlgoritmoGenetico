from poblacion import Poblacion

def datoAltura():
    while (True):

        try:
            altura = input("Ingresa el valor de la altura esperado -> ")
            altura = int(altura)
            break
        except:
            print(altura)
            print("No es un numero")

    return altura

promedioPoblacion = []
altura = datoAltura()



poblacion = Poblacion()
promedioPoblacion.append(poblacion.promedioPoblacion(altura))
iterable = 0
# poblacion.realizarTorneo(altura)



while(promedioPoblacion[iterable]!=0 ):
    poblacion.realizarTorneo(altura)
    promedioPoblacion.append(poblacion.promedioPoblacion(altura))
    print(poblacion.promedioPoblacion(altura))
    iterable+=1
    if(iterable%200==0):
        poblacion.mostrarPoblacion()
        poblacion = Poblacion()
        print("Nueva Poblacion")
    


poblacion.mostrarPoblacion()