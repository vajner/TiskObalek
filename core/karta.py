class Karta:
    UID = 0
    jmeno = ""
    prijmeni = ""
    datum_narozeni = ""
    
    def __init__(self, cislo=None, jmeno=None, platnost=None):
        self.cislo = cislo
        self.platnost = platnost
        self.jmeno = jmeno
        self.prijmeni = ""
        self.datum_narozeni = ""

    def __str__(self):
        return (
            f"Karta(cislo={self.cislo}, jmeno={self.jmeno}, prijmeni={self.prijmeni}, "
            f"datum_narozeni={self.datum_narozeni}, platnost={self.platnost})"
        )
