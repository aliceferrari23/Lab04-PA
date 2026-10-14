class Stand:
    def __init__(self,codice, superficie, padiglione, prezzo_base):
        self.codice = codice
        self.superficie = float(superficie)
        self.padiglione = padiglione
        self.prezzo_base = float(prezzo_base)
        self.espositore = None

    @property
    def disponibile(self):
        return self.espositore is None

    def calcola_prezzo(self):
        return self.prezzo_base

    def stato_str(self):
        if self.disponibile:
            return "Disponibile"
        else:
            return f"Assegnato a {self.espositore.codice}"

    def __eq__(self, other):
        if isinstance(other, Stand):
            return self.codice == other.codice
        return False

    def __lt__(self, other):
        return self.calcola_prezzo() < other.calcola_prezzo()