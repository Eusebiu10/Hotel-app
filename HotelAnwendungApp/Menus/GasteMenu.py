from Model.Gast import Gast

class GasteMenu:

    def __init__(self, ):
        self.gasteList = []

    #Setter for Gaste list
    def set_GasteList(self, gastelist):
        self.gasteList = gastelist

    #Getter for Gaste List
    def get_GastList(self):
        return self.gasteList

    #Append new Reservierung
    def append_reservierung(self, gastNummer, reservierung):
        self.gasteList[gastNummer].append_reservierung(reservierung)

    #Einfugen Gast
    def einfugen_Gast(self, vorname, nachname):
        gast = Gast()
        gast.set_vorname(vorname)
        gast.set_nachname(nachname)
        self.gasteList.append(gast)

    #Aktualisieren Nachname des Gast
    def aktualisieren_nachname(self, gastNummer, neueNachname):
        if gastNummer > len(self.gasteList) or gastNummer < 0:
            print("Diese Gast existiert nicht!")
        else:
            self.gasteList[gastNummer].set_nachname(neueNachname)

    #Aktualisieren Vorhname des Gast
    def aktualisieren_vorname(self, gastNummer, neueVorname):
        if gastNummer > len(self.gasteList) or gastNummer < 0:
            print("Diese Gast existiert nicht!")
        else:
            self.gasteList[gastNummer].set_vorname(neueVorname)

    #Loschen eines Gastes
    def loschen_gast(self, gastNummer):
        if gastNummer > len(self.gasteList) or gastNummer < 0:
            print("Diese Gast existiert nicht!")
        else:
            del(self.gasteList[gastNummer])

    #Anzeige die Liste von Gasten
    def zeige_gastListe(self):
        for obj in self.gasteList:
            print( "Nachname:", obj.get_nachname(), "Vorname:", obj.get_vorname() )
