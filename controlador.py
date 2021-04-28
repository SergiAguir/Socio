from socio import Socio

class Controlador:
    def __init__(self):
        self.listaSocios = {}
        self.productos = {"Naranja":10,"Oliva":20,"Caqui":5}

    def getNumSocios(self):
        return len(self.listaSocios)

    def getProductos(self):
        lista=""
        for i in self.productos:
            lista += i+"\n"
        return lista


    def existeSocio(self,idsocio):
        if idsocio in self.listaSocios.keys():
            return True
        else:
            return False

    def _check_dni(self,dni):
        letras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
        
        letraDNI = dni[-1].upper()
        numDNI = dni[:-1]

        if (letraDNI.isalpha() == False):
            return False
        if len(dni) != 9:
            return False
        else:
            letraCalculada = letras[int(numDNI)%23]
            if (letraDNI != letraCalculada):
                return False
        return True

    def existeDNI(self,dni):
        if dni in self.listaSocios.values():
            return True
        else:
            return False

    def addSocio(self,socio):
        if socio.getIdSocio() in self.listaSocios.keys():
            return False
        else:
            self.listaSocios[socio.getIdSocio()]=socio
            return True

    def delSocio(self,idsocio):
        if idsocio in self.listaSocios.keys():
            del self.listaSocios[idsocio]
            return True
        else:
            return False

    def listarSocios(self):
        res = ""
        for i in self.listaSocios.values():
            res += str(i.getIdSocio())+" "+i.getDNI()+" "+i.getNombre()+" "+i.getApellido()+" "+str(i.getFecha())+" "+str(i.getSaldo())+" "+str(i.getRegistros())+"\n"
        return res

    def recuperarSocio(self,idsocio):
        if idsocio in self.listaSocios.keys():
            socio = self.listaSocios[idsocio]
        return socio

    def addProducto(self,idsocio,producto,kilos):
        if idsocio in self.listaSocios:
            if producto in self.productos:
                self.listaSocios[idsocio].addProducto(producto,kilos)
                return True
        return False




    def actualizarSaldo(self,idsocio):
        saldo=0
        if idsocio in self.listaSocios:
            for clave,valor in self.listaSocios[idsocio].getRegistros().items():
                saldo+= self.productos[clave] * int(valor)

            self.listaSocios[idsocio].setSaldo(saldo)
            self.listaSocios[idsocio].delRegistros()
            return True
        return False

