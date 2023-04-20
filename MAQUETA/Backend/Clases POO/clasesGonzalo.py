class Personas:
    def __init__(self,nombre,email,tel):
        self.setNombre(nombre)
        self.setEmail(email)
        self.setTel(tel)

    def setNombre(self,nombre):
        if isinstance(nombre,str):
            self.nombre = nombre
        else: 
            raise Exception("setNombre: Ingrese un Nombre válido.")

    def setEmail(self,email):
        if isinstance(email,str) and "@" in email:
            self.email = email
        else: 
            raise Exception("setEmail: Ingrese un Email válido.")

    def setTel(self,tel):
        if isinstance(tel,int) and len(tel)>=10:
            self.tel = tel
        else: 
            raise Exception("setTel: Ingrese un telefono válido.")

    def getNombre(self):
        return self.nombre
    def getEmail(self):
        return self.email
    def getTel(self):
        return self.tel


#sub Clases

class Clientes(Personas):
    def __init__(self,nombre,email,tel,dni,direccion):
        Personas.__init__(self,nombre,email,tel)
        self.setDNI(dni)
        self.setDireccion(direccion)

    def setDNI(self,dni):
        if isinstance(dni,int) and len(dni)==8:
            self.dniCliente = dni
        else: 
            raise Exception("setDNI: Ingrese un dni válido.")
    def setDireccion(self,dir):
        if isinstance(dir,str):
            self.direccionCliente = dir
        else: 
            raise Exception("setDireccion: Ingrese una Dirección válida.")
    
    def getDni(self):
        return self.dniCliente
    def getDireccion(self):
        return self.direccionCliente
    
    def generarPedido(self):
        pass
    def actualizarPedido(self,pedido):
        pass
    def pagarFactura(self,factura):
        pass
    def cancelarPedido(self,pedido):
        pass
    def realizarReclamo(self,pedido):
        pass

class Empleado(Personas):
    horarios = ["turno mañana","turno siesta","turno tarde"]
    def __init__(self,nombre,email,tel,usuario,contraseña,horarios):
        Personas.__init__(self,nombre,email,tel)
        self.setUsuario(usuario)
        self.setPassword(contraseña)
        self.setHorarios(horarios) 

    def setUsuario(self,usuario):
        if isinstance(usuario,str):
            self.usuario = usuario
        else: 
            raise Exception("setUsuario: Ingrese un Usuario válido.")
    def setPassword(self,contraseña):
        if isinstance(contraseña,str):
            self.__password = contraseña
        else: 
            raise Exception("setPassword: Ingrese una contraseña válida.")
    def setHorarios(self,horario):
        if isinstance(horario,str) and horario.strip().lower() in  Empleado.horarios:
            self.horario = horario
        else: 
            raise Exception("setHorarios: Ingrese un Horario válido.")
    
    def getUsuario(self):
        return self.usuario
    def getHorario(self):
        return self.horario
    
    def registrarse(self):
        pass
    def login(self):
        pass
    def verificarLogin(self):
        pass


class Transportista(Empleado):
    def __init__(self, nombre, email, tel, usuario, contraseña, horarios,licencia):
        Empleado.__init__(nombre, email, tel, usuario, contraseña, horarios)
        self.setLicencia(licencia)
        
    def setLicencia(self,licencia):
        if isinstance(licencia,int):
            self.licencia = licencia
        else: 
            raise Exception("setLicencia: Ingrese una Licencia válida.")

    def getLicencia(self):
        return self.licencia
    
    def manejar(self,vehiculo):
        pass
    def despacharPaquetes(self):
        pass

class Administrativo(Empleado):
    def __init__(self, nombre, email, tel, usuario, contraseña, horarios):
        Empleado.__init__(nombre, email, tel, usuario, contraseña, horarios)
    
    def registrarPaquete(self):
        pass
    def entregarPaquete(self):
        pass
    def facturar(self,Factura):
        pass
    def manejarDevoluciones(self,pedido):
        pass