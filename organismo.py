import random;
class Organismo:
    
    def llenarOrganismo(self):
        organismo = []
        for i in range(16):
            organismo.append(random.randint(0,1));
        return organismo;
       
            
    
    
    def __init__(self):
        self.cromosoma = self.llenarOrganismo()
        
        
    def agregarR(self, valor:int):
            self.cromosoma.append(valor)
            
    def mostrarOrganismo(self):
        return self.cromosoma;

    
    def setCromosoma(self, nuevo):
       self.cromosoma = nuevo