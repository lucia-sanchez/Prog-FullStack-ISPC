class Factura:
    def __init__(self, codigo, fecha_factura, fecha_entrega, nombre_cliente, id_cliente, nombre_empleado, precio_producto):
        self.__Codigo = codigo
        self.__Fecha_factura = fecha_factura
        self.__Fecha_entrega = fecha_entrega
        self.__Nombre_cliente = nombre_cliente
        self.__Id_cliente = id_cliente
        self.__Nombre_empleado = nombre_empleado
        self.__Precio_producto = precio_producto
        self.__Precio_final = 0 

    def get_Codigo(self):
        return self.__Codigo

    def set_Codigo(self, codigo):
        self.__Codigo = codigo


    def get_Fecha_factura(self):
        return self.__Fecha_factura 

    def set_Fecha_factura(self, fecha_factura):
        self.__Fecha_factura= fecha_factura


    def get_Fecha_entrega(self):
        return self.__Fecha_entrega

    def set_Fecha_entraga(self, fecha_entrega):
        self.__Fecha_entrega = fecha_entrega


    def get_Nombre_cliente(self):
        return self.__Nombre_cliente

    def set_Nombre_cliente(self, nombre_cliente):
        self.__Nombre_cliente = nombre_cliente


    def get_Id_cliente(self):
        return self.__Id_cliente 

    def set_Id_cliente(self, id_cliente):
        self.__Id_cliente = id_cliente


    def get_Nombre_empleado(self):
        return self.__Nombre_empleado

    def set_Nombre_empleado(self, nombre_empleado):
        self.__Nombre_empleado = nombre_empleado


    def get_Precio_producto(self):
        return self.__Precio_producto

    def set_Precio_producto(self, precio_producto):
        self.Precio_producto= precio_producto


    def Precio_final(self):
        return (self.__Precio_producto * 0.21) + self.__Precio_producto
        


    def MostrarDatos (self):
        print('Codigo de factura: ' + str(self.__Codigo) + ' Fecha de factura: ' + str(self.__Fecha_factura) + ' Fecha de entrega ' + str(self.__Fecha_entrega) + ' Nombre del Cliente ' + self.__Nombre_cliente + ' Id del cliente ' + str(self.__Id_cliente) + ' Nombre del empleado: ' + self.__Nombre_empleado + ' Precio del producto: ' + str(self.__Precio_producto))


""" PROBANDO CON UNA CLASE LOS METODOS DESARROLLADOS"""


factura1 = Factura (1, '4/11/2022', '4/11/2022', "Jose", 45, "Pablo",6500)
factura1.MostrarDatos()
print(factura1.Precio_final())
