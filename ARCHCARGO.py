class Cargo:
    secuencia = 2
    cargos = [{"codigo":1,"cargo":"Gerente"}, {"codigo":2,"cargo":"Jefe"}]

    def __init__(self, descrip):
        Cargo.secuencia += 1
        self.codigo = Cargo.secuencia
        self.cargo = descrip

    def  registro(self):
        return {"codigo":self.codigo,"cargo":self.cargo}