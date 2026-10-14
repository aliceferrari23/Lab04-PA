import csv
from espositore import Espositore
from stand_premium import StandPremium
from stand_prese import StandPrese
from stand_standard import StandStandard


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome=nome
        self.stand = {}
        self.espositori = {}


    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome=nome



    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for riga in reader:
                    codice = riga[0]
                    if codice.startswith('ES'):
                        nome = riga[1]
                        cognome = riga[2]
                        self.espositori[codice] = Espositore(codice, nome, cognome)
                    else:
                        superficie = riga[1]
                        padiglione = riga[2]
                        prezzo = riga[3]
                        if len(riga) == 4:
                            self.stand[codice] = StandStandard(codice, superficie, padiglione, prezzo)
                        elif len(riga) == 5:
                            extra = riga[4]
                            if extra.isdigit():
                                self.stand[codice] = StandPrese(codice, superficie, padiglione, prezzo, extra)
                            else:
                                self.stand[codice] = StandPremium(codice, superficie, padiglione, prezzo, extra)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} non trovato.")


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        if codice_stand not in self.stand:
            raise ValueError(f"Lo stand {codice_stand} non esiste.")
        if codice_espositore not in self.espositori:
            raise ValueError(f"L'espositore {codice_espositore} non esiste.")

        stand = self.stand[codice_stand]
        espositore = self.espositori[codice_espositore]

        if not stand.disponibile:
            raise ValueError(f"Lo stand {codice_stand} è già occupato.")
        if espositore.stand_assegnato is not None:
            raise ValueError(f"L'espositore {codice_espositore} ha già uno stand assegnato.")

        stand.espositore = espositore
        espositore.stand_assegnato = stand

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        if not self.espositori:
            print("Nessun espositore registrato.")
            return

        for espositore in self.espositori.values():
            if espositore.stand_assegnato:
                info_stand = espositore.stand_assegnato.codice
            else:
                info_stand= "Nessuno stand"

            print(f"{espositore} -  {info_stand}")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(list(self.stand.values()))
