from socio import Socio
from controlador import Controlador
from datetime import datetime

con = Controlador()

while True:
    print("El numero total de socios es ",con.getNumSocios())
    print("1.- Alta Socio")
    print("2.- Baja Socio")
    print("3.- Listar Socios")
    print("4.- Registrar Producto")
    print("5.- Actualizar Saldo")
    print("6.- Ficha de socio")
    print("7.- Salir")


    op = int(input("Selecciona una opcion: "))

    if op == 1:
        while True:
            try:
                idsocio = int(input("Introduce el id del Socio: "))
                    
                socioExsiste = con.existeSocio(idsocio)

                if socioExsiste == True:
                    print("----------------------------")
                    print("Ya exsiste el Id del socio!!")
                    print("----------------------------")
                else:
                    break
            except ValueError:
                print("------------------------")
                print("El Id socio no es valido")
                print("------------------------")

        while True:
            try:
                dni = str(input("Introduce el DNI: "))

                compDNI = con._check_dni(dni)

                if compDNI == False:
                    print("---------------------------------")
                    print("El DNI introducido no es correcto")
                    print("---------------------------------")
                else:
                    dniExsiste = con.existeDNI(dni)
                    if dniExsiste == True:
                        print("-------------------")
                        print("El DNI ya exsiste!!")
                        print("-------------------")
                    else:
                        break
            except ValueError:
                print("-------------------")
                print("El DNI no es valido")
                print("-------------------")

        while True:
            try:
                nombre = str(input("Introduce el nombre: "))
                if nombre == "":
                    print("----------------------------------")
                    print("El nombre no puede estar en blanco")
                    print("----------------------------------")
                else:
                    break
            except ValueError:
                print("----------------------")
                print("El nombre no es valido")
                print("----------------------")

        while True:
            try:
                apellido = str(input("Introduce el apellido: "))
                if apellido == "":
                    print("------------------------------------")
                    print("El apellido no puede estar en blanco")
                    print("------------------------------------")
                else:
                    break
            except ValueError:
                print("------------------------")
                print("El apellido no es valido")
                print("------------------------")

        while True:
            try:
                fecha = datetime.now()
                fechaForm = fecha.strftime("%d/%m/%Y %H:%M")
                print("--------------")
                print("Fecha anyadida")
                print("--------------")
                break
            except ValueError:
                print("---------------------")
                print("La fecha no es valida")
                print("---------------------")

        socio = Socio(idsocio,dni,nombre,apellido,fecha)
        con.addSocio(socio)
        print("--------------------------------------------------------------")
        print("El socio ",socio.getIdSocio()," ha sido anyadido correctamente")
        print("--------------------------------------------------------------")

    if op == 2:
        idsocio = int(input("Introduce idsocio: "))

        socioExsiste = con.existeSocio(idsocio)

        if socioExsiste == True:
            con.delSocio(idsocio)
            print("-----------------------------------------------------------")
            print("El socio con id ",idsocio," ha sido eliminado correctamente")
            print("-----------------------------------------------------------")
        else:
            print("---------------------")
            print("El socio no exsiste!!")
            print("---------------------")

    if op == 3:
        print("Lista de socios \n",con.listarSocios())

    if op == 4:
        idsocio = int(input("Introduce un idsocio: "))

        print(con.getProductos())
        
        while True:

            op2 = int(input("Que producto quieres registrar?: "))

            if op2 == 1:
                producto = "Naranja"
                kilo = int(input("Introduce los kilos: "))

                regis = con.addProducto(idsocio,producto,kilo)

                if con.addProducto(idsocio,producto,kilo):
                    print("Producto registrado!")
                break

            if op2 == 2:
                producto = "Oliva"
                kilo = int(input("Introduce los kilos: "))


                regis = con.addProducto(idsocio,producto,kilo)

                if con.addProducto(idsocio,producto,kilo):
                    print("Producto registrado!")
                break

            if op2 == 3:
                producto = "Caqui"
                kilo = int(input("Introduce los kilos: "))

                regis = con.addProducto(idsocio,producto,kilo)

                if con.addProducto(idsocio,producto,kilo):
                    print("Producto registrado!")
                break

    if op == 5:
        idsocio = int(input("Introduce un Id socio: "))

        if con.actualizarSaldo(idsocio):
            print("Saldo actualizado correctamente!")


    if op == 6:
        idsocio = int(input("Introduce un idsocio: "))

        socio = Socio(0,"","","","")

        socio = con.recuperarSocio(idsocio)

        print("Id socio: ",socio.getIdSocio())
        print("DNI: ",socio.getDNI())
        print("Nombre: ",socio.getNombre())
        print("Apellido: ",socio.getApellido())
        print("Fecha: ",socio.getFecha())
        print("Saldo: ",socio.getSaldo())
        print("Registros: ",socio.getRegistros())



    if op == 7:
        print("Adios!!")
        break

