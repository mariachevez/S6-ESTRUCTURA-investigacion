class Departamento:
    secuencia= 2
    departamentos = [{"codigo":1, "descripcion":"Recursos humanos"},
                     {"codigo":2, "descripcion":"Comité de dirección"}]
    
    def __init__(self, descrip):
        Departamento.secuencia += 1
        self.codigo = Departamento.secuencia
        self.departamento = descrip

    def  registro(self):
        return {"codigo":self.codigo,"descripcion":self.departamento}