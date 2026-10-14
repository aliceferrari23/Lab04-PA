from stand import Stand

class StandStandard(Stand):
    def __str__(self):
        return f"{self.codice}: Standard | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo()}€ - {self.stato_str()}"