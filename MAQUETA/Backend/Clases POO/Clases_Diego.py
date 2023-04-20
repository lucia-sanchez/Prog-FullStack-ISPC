class Servicios:
    def __init__(self, codigo, nombre, descripción, precio):
        self.__Codigo=codigo
        self.__Nombre=nombre
        self.__Descripción=descripción
        self.__Precio=precio
        self.__Estado=True
    
    # Getters (métodos GET)
    def get_Codigo(self):
        return self.__Codigo
    
    def get_Nombre(self):
        return self.__Nombre
    
    def get_Descripción(self):
        return self.__Descripción
    
    def get_Precio(self):
        return self.__Precio    
    
    # Setters (método SET)
    def set_Codigo(self, codigo):
        self.__Codigo=codigo
        
    def set_Nombre(self, nombre):
        self.__Nombre=nombre 
        
    def set_Descripción(self, descripción):
        self.__Descripción=descripción
        
    def set_Precio(self, codigo):
        self.__Precio=codigo  
        
    # Estado del servicio:
    def Estados(self,estado):
        self.__Estado=estado
        if(self.__Estado):
            return "El Servicio esta Activo"
        else:
            return "El Servicio esta inactivo"
    
    # Mostrar resultados:
    def Resultados(self):
        Mostrar_si = self.__Estado
        if(Mostrar_si==True): 
            print("El Servico de codigo",self.__Codigo, "con nombre de ", self.__Nombre,", tiene los siguientes datos:")
            print("Descripción:",self.__Descripción,". El precio es de:",self.__Precio)
        else:
            print("El servicio no puede mostrar resultados")

#PRUEBA DE LA CLASE SERVICIOS

Servicio1 = Servicios(1427,"Envios","Envio de un paquete",5000)

print(Servicio1.get_Codigo())
print(Servicio1.get_Nombre())
print(Servicio1.get_Descripción())
print(Servicio1.get_Precio())
print(Servicio1.Estados(False))
Servicio1.Resultados()


class Paquete:
    def __init__(self, cod_paquete, contenido, peso, volumen, precio_paquete, tipo_transporte):
        self.__codigo = cod_paquete
        self.__contenido = contenido
        self.__peso = peso
        self.__volumen = volumen
        self.__precio = precio_paquete
        self.__transporte = tipo_transporte
    
    def get_codigo(self):
        return self.__codigo
    def get_contenido(self):
        return self.__contenido
    def get_peso(self):
        return self.__peso
    def get_volumen(self):
        return self.__volumen
    def get_precio(self):
        return self.__precio
    def get_tipo_transporte(self):
        return self.__transporte

    def set_codigo(self,cod):
        self.__codigo=cod
    def set_contenido(self,cont):
        self.__contenido=cont
    def set_peso(self,pes):
        self.__peso=pes
    def set_volumen(self,vol):
        self.__volumen=vol
    def set_precio(self,pre):
        self.__precio=pre
    def set_tipo_transporte(self,transp):
        self.__transporte=transp    
    
    #Mostrar resultado:
    def Mostrar(self):
        print("El paquete de codigo:",self.__codigo,"contiene",self.__contenido,"y tiene un peso total de",
              self.__peso,"KG",",con un volumen de",self.__volumen,"m3",".Su precio es:","$",self.__precio,"y el tipo de transporte es:",self.__transporte)
    
#PRUEBA DE LA CLASE PAQUETE

Paquete1 = Paquete(1002,"Heladera",58,0.63,120000,"Camion")

Paquete1.Mostrar()
Paquete1.set_contenido("Televisor")
print("Cambiamos el contenido por:",Paquete1.get_contenido())
Paquete1.Mostrar()

class Destino:
    def __init__(self, pais, provincia, cod_postal, direccion, nombre_cliente):
        self.__pais=pais
        self.__prov=provincia
        self.__postal=cod_postal
        self.__direccion=direccion
        self.__nombre=nombre_cliente
    
    def get_pais(self):
        return self.__pais
    def get_prov(self):
        return self.__prov
    def get_postal(self):
        return self.__postal
    def get_direccion(self):
        return self.__direccion
    def get_nombre(self):
        return self.__nombre
    
    def set_pais(self,pais):
        self.__pais=pais
    def set_prov(self,prov):
        self.__prov=prov
    def set_postal(self,postal):
        self.__postal=postal
    def set_direccion(self,direc):
        self.__direccion=direc
    def set_nombre(self,nombre):
        self.__nombre=nombre
        
    #Mostrar datos del destino
    def Mostrar_destino(self):
        print("El destino se situa en",self.__pais,"en la provincia de",self.__prov,"con codigo postal",self.__postal,"y tiene la dirección  en",self.__direccion,". Donde vive el cliente llamado:",self.__nombre)

#PRUEBA DE LA CLASE DESTINO

Destino1 = Destino("Argentina","Buenos Aires",2356,"Mitre 8080","Alicia Alvarez") 

Destino1.Mostrar_destino() 