from datetime import datetime

from Model.Reservierung import Reservierung


class Gast:

    def __init__(self):
        self.reservierungen = []

    # Setters
    def set_vorname(self, vorname):
        self.vorname = vorname

    def set_nachname(self, nachname):
        self.nachname = nachname

    def set_reservierung(self, reservierung):
        self.reservierungen.append( reservierung )

    # Getters
    def get_vorname(self):
        return self.vorname

    def get_nachname(self):
        return self.nachname

    def get_reservierungen(self):
        return self.reservierungen

    # Mach eine Reservierung
    def mache_reservierung(self, zimmerNummer, gasteAnzahl, zeitRaum, zimmerListe, gasteListe):
        reservierung = Reservierung()
        ok = 0
        for obj in zimmerListe:
            if int(obj.get_nummer()) == zimmerNummer:
                if int(obj.get_anzahl()) >= gasteAnzahl:
                    print( obj.get_nummer() )
                    print( obj.get_anzahl() )
                    for obj1 in gasteListe:
                        for obj2 in obj1.get_reservierungen():
                            if int(obj2.get_zimmer().get_nummer()) == zimmerNummer and datetime.strptime(obj2.get_zeitraum()[0:13], "%Y:%m:%d %H" ) <= datetime.strptime(zeitRaum[0:13], "%Y:%m:%d %H") <= datetime.strptime(obj2.get_zeitraum()[16:29], "%Y:%m:%d %H" ):
                                ok = -1
                    if ok == 0:
                        reservierung.set_zimmer( obj )
                        reservierung.set_gastenummer( gasteAnzahl )
                        reservierung.set_zeitraum( zeitRaum )
                        ok = 1
                    else:
                        print('Zimmer ist bereits belegt')
        if ok == 1:
            self.reservierungen.append( reservierung )
            print('Erfolgreiche Buchung! Zimmer Nummer:', zimmerNummer, 'Gaste Anzahl:', gasteAnzahl, 'Zeit Raum:', zeitRaum)
        else:
            print('Falsch angabe!')