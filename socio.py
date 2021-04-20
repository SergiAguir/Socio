class Socio:
    def __init__(self,idsocio,dni,nombre,apellido,fecha):
        self.idsocio = idsocio
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha
        self.saldo = 0
        self.registros = []

    def getIdSocio(self):
        return self.idsocio

    def getDNI(self):
        return self.dni

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getFecha(self):
        return self.fecha

    def getSaldo(self):
        return self.saldo

    def getRegistros(self):
        return self.registros

    def setIdSocio(self,idsocio):
        self.idsocio = idsocio

    def setDNI(self,dni):
        self.dni = dni

    def setNombre(self,nombre):
        self.nombre = nombre

    def setApellido(self,apellido):
        self.apellido = apellido

    def setFecha(self,fecha):
        self.fecha = fecha

    def setSaldo(self,saldo):
        self.saldo = saldo

    def setRegistros(self,registros):
        self.registros = registros
