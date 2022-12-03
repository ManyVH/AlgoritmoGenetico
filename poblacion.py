import random

from organismo import Organismo


class Poblacion:
    poblacion = []
    
    def __init__(self):
        # Llenar Poblacion
        for i in range(100):
            self.poblacion.append(Organismo())
           
            
       
        self.calcularValores()
    
    def calcularValores(self):
        # Cacular valores con la ecuacion de cada organismo en la poblacion
        for organismo in self.poblacion:
            resultadosNumericos = []
            factor = 3
            valorParaRN = 0

            for bit in organismo.mostrarOrganismo():
                valorParaRN += (bit * (2 ^ factor))
                factor -= 1
                if (factor == 0):
                    resultadosNumericos.append(valorParaRN)
                    factor = 5

            organismo.agregarR(resultadosNumericos[0]+(
                resultadosNumericos[1]*resultadosNumericos[2])-(5*(resultadosNumericos[2] ^ 2)))
            
            
    def realizarTorneo(self, altura):
        nuevaP = []
        for i in range(100):
            ##Cambiar el elegir para que no se pacen referencias  
            
            torneo = random.sample(self.poblacion,k=5)
            nuevaP.append(self.clasificar(torneo,altura)) 
            # self.mostrarPoblacion()
            # print("-----------------------------------------------------------")
            for x in self.poblacion:
                if(len(x.mostrarOrganismo())==18):
                    x.mostrarOrganismo().pop()
            # self.mostrarPoblacion()

        
        self.poblacion = nuevaP
        self.calcularValores()
        #self.mostrarPoblacion()
        # for x in nuevaP:
        #     print(x.mostrarOrganismo())
            
    def mostrarPoblacion(self):
        for x in self.poblacion:
            print(x.mostrarOrganismo())

    def clasificar(self, torneo, altura):
        listaCrosomosas = []
        for i in range(len(torneo)):
            #Se calcula en sacando el valor 48 donde esta el resultado del organismo
            torneo[i].agregarR(abs(torneo[i].cromosoma[len(torneo[i].cromosoma)-1]-altura))
            #se saca de la posición 49 la diferencia entre la altura esperada y el resultado del organismo
            listaCrosomosas.append((i,torneo[i].mostrarOrganismo()[17]))
        
        listaCrosomosas =sorted(listaCrosomosas,key=lambda listaCrosomosas: listaCrosomosas[1])
        # print(listaCrosomosas)
        # print(torneo[listaCrosomosas[0][0]].mostrarOrganismo())
        # print(torneo[listaCrosomosas[1][0]].mostrarOrganismo())
        
        return self.mutacion(torneo[listaCrosomosas[0][0]].mostrarOrganismo(),torneo[listaCrosomosas[1][0]].mostrarOrganismo())
    
    def mutacion(self,individuo_1,individuo_2):
        nuevoOrganismo = Organismo()
        crosomosaNuevo = []
        for i in range(16):
            if(i<=4):
                crosomosaNuevo.append(individuo_1[i])
            elif(i<=10):
                crosomosaNuevo.append(individuo_2[i])
            else:
                crosomosaNuevo.append(individuo_1[i])
        
        # print(crosomosaNuevo)
        for i in range(len(crosomosaNuevo)):  
            if(random.randint(0,100)>=95):
                if(crosomosaNuevo[i]==1):
                    crosomosaNuevo[i] = 0
                else:
                    crosomosaNuevo[i] = 1
        # print(crosomosaNuevo)
        nuevoOrganismo.setCromosoma(crosomosaNuevo)
        return nuevoOrganismo
    
    
    def promedioPoblacion(self, altura):
        promedio = 0
        for i in self.poblacion:
            promedio+= abs( i.mostrarOrganismo()[len(i.mostrarOrganismo())-1]-altura)
        return promedio/100
