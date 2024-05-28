class Personaje:
    
    #ATRIBUTOS
    #nombre - poder_pelea - habilidad - puede_volar - usa_nanotecnologia
    
    
    #METODOS
    #constructor
    def __init__(self, nombre: str, poder: int, habilidad: str, vuela: bool, nano: bool):
        self.nombre = nombre
        self.poder_pelea = poder
        self.habilidad = habilidad
        self.puede_volar = vuela
        self.usa_nanotecnologia = nano
    
    def describirse(self):
        descripcion = (f"{self.nombre}-{self.poder_pelea}-{self.habilidad}")
        if self.usa_nanotecnologia:
            descripcion += "-Usa nanotecnologia"
        else:
            descripcion += "-No usa nanotecnologia"
        descripcion += "\n" + "*"*30
        return descripcion
    
    def volar(self, altura, velocidad):
        if self.puede_volar:
            print(f"{self.nombre}: estoy volando a {altura} mts a una velocidad de: {velocidad} KM/h")
        else:
            print(f"{self.nombre} aun no puede volar")
    
    def atacar(self, enemigo: "Personaje"):
        if self.poder_pelea > enemigo.poder_pelea:
            print(f"Gano: {self.nombre}")
            self.poder_pelea -= enemigo.poder_pelea
            enemigo.poder_pelea = 0
        elif self.poder_pelea < enemigo.poder_pelea:
            print(f"Gano: {enemigo.nombre}")
            enemigo.poder_pelea -= self.poder_pelea
            self.poder_pelea = 0
        else:
            print(f"{self.nombre} y {enemigo.nombre} empataron")
            self.poder_pelea *= 0.9
            enemigo.poder_pelea *= 0.9