class Boligrafo:
    
    def __init__(self, grosor_punta: str, color: str):
        self.capacidad_tinta_maxima = 100
        self.cantidad_tinta = 80
        self.grosor_punta = grosor_punta
        self.color = color
    
    
    def escribir(self, texto):
        if self.grosor_punta == "Fino":
            self.cantidad_tinta = self.cantidad_tinta - len(texto)
            return f"Tinta restante {self.cantidad_tinta}"
        elif self.grosor_punta == "Grueso":
            self.cantidad_tinta = self.cantidad_tinta - (len(texto) * 2)
            return f"Tinta restante {self.cantidad_tinta}"
    
    def recargar(self, cantidad):
        self.cantidad_tinta += cantidad
        if self.cantidad_tinta > self.capacidad_tinta_maxima:
            sobrante = self.cantidad_tinta - self.capacidad_tinta_maxima
            return f"La cantidad recargada exedio y sobro {sobrante}"
        else:
            return f"Lapicera recargada {self.cantidad_tinta}"


