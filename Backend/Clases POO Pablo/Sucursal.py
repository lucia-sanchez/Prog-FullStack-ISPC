class Sucursales:
    def __init__(self, numero, direccion, telefono, horario):
        self.__Numero = numero
        self.__Direccion = direccion
        self.__Telefono = telefono
        self.__Horario = horario

    def get_Numero(self):
        return self.__Numero

    def get_Direccion(self):
        return self.__Direccion

    
    def get_Telefono(self):
        return self.__Telefono
    

    def get_Horario(self):
        return self.__Horario

    def set_Horario (self, horario):
        self.__Horario = horario

    def __str__(self):
        return "Sucursal Numero:" + self.__Numero + "Direccion :" + self.__Direccion + "Telefono:" + self.__Telefono + "Horarios de atencion:" + self.__Horario


"""PROBANDO CON UNA CLASE LOS METODOS DESARROLLADOS"""

        
sucursal_1 = Sucursales ("1  ", "Av sabattini 1900  ", "123456  ", "09:00 A 17:00")
print(sucursal_1)
print(sucursal_1.get_Horario())
sucursal_1.set_Horario("10:00 A 15:00")
print(sucursal_1.get_Horario())
