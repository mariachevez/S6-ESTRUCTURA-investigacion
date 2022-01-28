class Empleado:
    secuencia = 1
    Empleados= [{"codigo":1,"nombre":"Maria","cedula":"0992269847","cargo":1,"departamento":1,"sueldo":"360.00"},
                {"codigo":2,"nombre":"Juan","cedula":"0992095329","cargo":2,"departamento":2,"sueldo":"425.00"}]
    
    def __init__(self,nombre,cedula,codCargo,codDepartamento,sueldo):
        Empleado.secuencia += 1
        self.codigo = Empleado.secuencia
        self.nombre = nombre
        self.cedula= cedula
        self.cargo = codCargo
        self.departamento = codDepartamento
        self.sueldo = sueldo

    def  registro(self):
        return {"codigo":self.codigo,"nombre":self.nombre,"cedula":self.cedula,
        "cargo":self.cargo,"departamento":self.departamento,"sueldo":self.sueldo}