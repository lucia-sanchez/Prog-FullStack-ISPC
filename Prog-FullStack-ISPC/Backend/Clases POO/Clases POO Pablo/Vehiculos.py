class Vehiculos:
    def __init__(self,marca, color, modelo, año, capacidad_carga, ubicacion):
          self.__Marca = marca
          self.__Color = color 
          self.__Modelo = modelo
          self.__Año = año
          self.__Capacidad_carga = capacidad_carga
          self.__Ubicacion = ubicacion
          self.__Disponibilidad = True


    def get_Marca(self):
        return self.__Marca
    


    def get_Color(self):
        return self.__Color 

    def set_Color(self, color):
        self.__Color = color



    def get_Modelo(self):
        return self.__Modelo 


    def get_Año(self):
        return self.__Año 


    def get_Capacidad_carga(self):
        return self.__Capacidad_carga

    


    def get_Ubicacion(self):
        return self.__Ubicacion

    def set_Ubicacion(self, ubicacion):
        self.__Ubicacion = ubicacion




    def en_servicio (self):
        self.__Disponibilidad = False

    def estado (self):
        if (self.__Disponibilidad == False):
            return "El vehiculo se encuentra en servicio"
        else:
            return  "El vehiculo se encuentra disponible"


    def MostrarDatos (self):
        print("La marca del vehiculo es: " + self.__Marca + " modelo: " + self.__Modelo + " año " + str(self.__Año) + " color " + self.__Color + " Capacidad de carga" + self.__Capacidad_carga)
        

"""PRBANDO CON UNA CLASE LOS METODOS DESARROLLADOS"""
         

vehiculo1 = Vehiculos("Fort","Rojo","Ka",2015 ,"Una tonelada ","Sucursal Central")

print(vehiculo1.get_Ubicacion())
vehiculo1.set_Ubicacion("Cordoba")
print(vehiculo1.get_Ubicacion())
print(vehiculo1.estado())
vehiculo1.en_servicio()
print(vehiculo1.estado())
print(vehiculo1.get_Año())
print(vehiculo1.get_Color())
vehiculo1.set_Color("Azul")
print(vehiculo1.get_Color())
vehiculo1.MostrarDatos()
