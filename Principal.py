from ARCHMENU import Menu
from ARCHCARGO import Cargo
from ARCHDEPA import Departamento
from ARCHEMPLE import Empleado

def Consultar_Datos_AR(cod,indicador):
    res = ""
    if indicador == 1: 
        for pos in range(0,len(Cargo.cargos)):
            vcar = Cargo.cargos[pos]
            if vcar["codigo"] == cod:
                res = vcar["cargo"]
    elif indicador == 2:
        for pos in range(0,len(Departamento.departamentos)):
            vdep = Departamento.departamentos[pos]
            if vdep["codigo"] == cod:
                res = vdep["descripcion"]
    return res

def validar(valor,ind):
        if len(valor)>=ind and len(valor)<=20:
            if exist(valor, ind) == True:
                if ind != 3:
                    input("Datos ingresados satisfactoriamente, presione ENTER para continuar...")
                    return valor
                else:
                    return valor
            else:
                mesage_error(1)
                return ""
        else:
            mesage_error(0)
            return ""

def exist(valor, ind):
    i = True
    if ind == 1:
        for rep in Cargo.cargos:
            if rep["cargo"].title() == valor.title():
                i = False
    elif ind == 5:
        for rep in Departamento.departamentos:
            if rep["descripcion"].title() == valor.title():
                i = False
    return i

def sueld(valor):
        try:
            float(valor)
            return True
        except:
            return False

def mesage_error(ind):
    if ind == 2:
        print("El dato no existe, ingrese uno existente o cree uno nuevo.")
    elif ind == 1:
        print("El dato ya está creado, ingrese uno nuevo.")
    elif ind == 0:
        print("La entrada es incorrecta, cumpla con los términos.")
    elif ind == -1:
        print("Ingrese correctamente el valor con sus decimales [0000.00].")     

menupr = Menu()
lista = ["1) Cargo","2) Departamento","3) Empleados","4) Salir"]
lista2 = ["1) Ingreso","2) Consulta","3) Regresar al menú principal"]
dc = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','á','é','í','ó','ú',' ')
dn = ('0','1','2','3','4','5','6','7','8','9','0','.')
opcion=""

while opcion != "4":
    menupr.cls()
    opcion = menupr.menu(lista,"Menu Ficha Personal")
    opc1=""
    if opcion == "1":
        while opc1 != "3":
            menupr.cls()
            opc1 = menupr.menu(lista2,"MANTENIMIENTO DE CARGOS")
            menupr.cls()
            if opc1 == "1":
                print("*"*20,"INGRESO DE CARGOS","*"*20)
                cargnom = ""
                while len(cargnom)<1 or len(cargnom)>20:
                    cargnom = input("Cargo: ")
                    for per in str(cargnom):
                        if per.lower() not in dc:
                            cargnom = ""
                            break
                    cargnom = validar(cargnom,1)           
                carg = Cargo(cargnom.title())
                Cargo.cargos.append(carg.registro())
            elif opc1 == "2":
                print("*"*20,"LISTADO DE CARGOS","*"*20)
                print(" "*10,"[  Codigo  ]"," "*6,"[  Descripcion  ]")
                for i in Cargo.cargos:
                    cod = i["codigo"]
                    car = i["cargo"]
                    print(" "*15,cod," "*12,car)
                print("*"*59)
                input("Presione ENTER para continuar...")
    elif opcion == "2":
        while opc1 != "3":
            menupr.cls()
            opc1 = menupr.menu(lista2,"MANTENIMIENTO DE DEPARTAMENTOS")
            menupr.cls()
            if opc1 == "1":
                print("*"*20,"INGRESO DE DEPARTAMENTOS","*"*20)
                deparnom = ""
                while len(deparnom)<5 or len(deparnom)>20:
                    deparnom = input("Departamento: ")
                    for per in str(deparnom):
                        if per.lower() not in dc:
                            deparnom=""
                            break
                    deparnom = validar(deparnom,5)
                depar = Departamento(deparnom.title())
                Departamento.departamentos.append(depar.registro())
            elif opc1 == "2":
                print("*"*12,"LISTADO DE DEPARTAMENTOS","*"*12)
                print(" "*3,"[ Codigo ]"," "*6,"[      Descripcion     ]")
                for i in Departamento.departamentos:
                    cod = i["codigo"]
                    des = i["descripcion"]
                    print(" "*7,cod," "*13,des," "*(15-len(des)))
                input("Presione ENTER para continuar...")
    elif opcion == "3":
        while opc1 != "3":
            menupr.cls()
            opc1 = menupr.menu(lista2,"MANTENIMIENTO DE EMPLEADOS")
            menupr.cls()
            if opc1 == "1":
                print("*"*20,"INGRESO DE EMPLEADOS ","*"*20)
                nombre = ""
                while len(nombre)<3 or len(nombre)>20:
                    nombre = input("Nombre        : ")
                    for per in str(nombre):
                        if per.lower() not in dc:
                            nombre=""
                            break
                    nombre = validar(nombre,3)
                cedula = ""
                while len(cedula) != 10 or cedula[0] != "0":
                    cedula = input("Cedula        : ")
                    if len(cedula) != 10 or cedula[0] != "0":
                        mesage_error(0)
                cb = False
                while cb == False:
                    cargo = input("Cargo         : ")
                    if cargo.isdigit() == True:
                        if Consultar_Datos_AR(int(cargo), 1) == "":
                            mesage_error(2)
                        else:
                            cb = True
                    else:
                        mesage_error(0)
                        cb = False
                print(Consultar_Datos_AR(int(cargo), 1))
                cb = False
                while cb == False:
                    departamento = input("Departamento  : ")
                    if departamento.isdigit() == True:
                        if Consultar_Datos_AR(int(departamento), 2) == "":
                            mesage_error(2)
                        else:
                            cb = True
                    else:
                        mesage_error(0)
                        cb = False
                print(Consultar_Datos_AR(int(departamento), 2))
                sueldo = ""
                ct=0
                while sueldo == "":
                    sueldo = input("Sueldo        : ")
                    if sueldo != "":
                        for per in sueldo:
                            if per not in dn:
                                mesage_error(-1)
                                sueldo = ""
                        if sueldo !="":        
                            try:
                                float(sueldo)
                            except:
                                mesage_error(-1)
                                sueldo = ""
                                break
                    else:
                        mesage_error(-1)
                        sueldo = ""
                if '.' not in sueldo:
                    sueldo = sueldo + ".00"
                else:
                    for i in sueldo:
                        if i == '.':
                            cb = False
                        if cb == False:
                            ct+= 1
                    sueldo = sueldo+"0"
                    if ct > 2:
                        sueldo = sueldo[0:sueldo.find(".")+3]
                arcar = Empleado(nombre.title(), cedula, int(cargo), int(departamento), sueldo)
                Empleado.Empleados.append(arcar.registro())
                input("Datos ingresados satisfactoriamente, presione ENTER para continuar...")
            elif opc1 == "2":
                print("*"*50,"LISTADO DE EMPLEADOS","*"*50)
                print("[   Código   ]", " "*3, "[   Nombre   ]", " "*4, "[  Cedula  ]", " "*6, "[     Cargo     ]", " "*4, "[   Departamento   ]", " "*5, "[  Sueldo  ]")
                for le in Empleado.Empleados:
                    cod = le["codigo"]
                    nom = le["nombre"]
                    ced = le["cedula"] 
                    car = le["cargo"]
                    car1 = Consultar_Datos_AR(car, 1)
                    dep = le["departamento"]
                    dep1 = Consultar_Datos_AR(dep, 2)
                    sue = le["sueldo"]
                    print(" "*5,cod," "*(11-len(str(cod))),nom," "*(19-len(nom)),ced," "*(17-len(ced)),car1, " "*(21-len(str(car1))),dep1, " "*(25-len(dep1)), sue)
                input("Presione ENTER para continuar...")
    elif opcion == "4":
        print("Está saliendo del programa...\n") 
print("Ha salido del programa.")