import os
class Menu:
    def __init__(self):
        pass

    def menu(self,opciones,titulo):
        print("*"*20,titulo,"*"*20)
        for opcion in opciones:
            print(opcion)
        opc = input("Elija Opcion[1...{}]: ".format(len(opciones)))
        return opc
    
    def cls(self):
        os.system("cls")