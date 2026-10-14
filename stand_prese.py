from stand import Stand

class StandPrese(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, prese_extra):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.prese_extra = int(prese_extra)

    def calcola_prezzo(self):
        return self.prezzo_base*(1+0.07*self.prese_extra)

    def __str__(self):
        return f"{self.codice}: Prese Extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo()}€ - Prese aggiuntive: {self.prese_extra} - {self.stato_str()}"