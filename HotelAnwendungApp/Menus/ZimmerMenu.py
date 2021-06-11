from Model.Zimmer import Zimmer


class ZimmerMenu:

    def __init__(self, ):
        self.zimmerListe = []

    # Setter for Zimmer list
    def set_zimmerListe(self, zimmerliste):
        self.zimmerListe = zimmerliste

    # Getter for Zimmer List
    def get_zimmerList(self):
        return self.zimmerListe

    # Einfugen Zimmer
    def einfugen_zimmer(self, nummer, anzahl, preis, farbe, meerblick):
        ok = 1
        for obj in self.zimmerListe:
            if obj.get_nummer() == nummer:
                ok = 0
                break
        if ok == 1:
            zimmer = Zimmer()
            zimmer.set_nummer(nummer)
            zimmer.set_anzahl(anzahl)
            zimmer.set_preis(preis)
            zimmer.set_farbe(farbe)
            zimmer.set_meerblick(meerblick)
            self.zimmerListe.append(zimmer)
        else:
            print('Existierte Zimmer Id!')

    # Aktualisieren Nachname des zimmer
    def aktualisieren_preis(self, zimmerNummer, neuePreis):
        ok = 0
        for obj in self.zimmerListe:
            if obj.get_nummer() == zimmerNummer:
                obj.set_preis(neuePreis)
                ok = 1
        if ok == 0:
            print("Bitte geben Sie eine gültige Zimmernummer ein!")

    #Loschung eines zimmers
    def loschen_zimmer(self, zimmerNummer):
        ok = 0
        index = 0
        for i in range(len(self.zimmerListe)):
           if self.zimmerListe[i].get_nummer() == zimmerNummer:
              index = i
              ok = 1
              i = len(self.zimmerListe)
        if ok == 0:
           print( "Bitte geben Sie eine gültige Zimmernummer ein!" )
        else:
           del(self.zimmerListe[index])

    #Anzeige die Liste von zimmern
    def zeige_zimmerListe(self):
        for obj in self.zimmerListe:
           print( "ID:", obj.get_nummer(), "Anzahl:", obj.get_anzahl(), "Preis:", obj.get_preis()
                  , "Farbe:", obj.get_farbe(),"Meerblick:", obj.get_meerblick() )
