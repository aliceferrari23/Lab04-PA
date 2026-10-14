from stand import Stand

class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.posizione = posizione

    def calcola_prezzo(self):
        return self.prezzo_base * 1.30

    def __str__(self):
        return (f"{self.codice}: Premium | {self.superficie} mq - Padiglione {self.padiglione} - "
                f"Prezzo {self.calcola_prezzo():.2f}€ - Posizione: {self.posizione} - {self.stato_str()}")