from datetime import datetime


class Functions:

    def __init__(self):
        pass

    def set_zimmerMenu(self, zimmerMenu):
        self.zimmerMenu = zimmerMenu

    def set_gasteMenu(self, gasteMenu):
        self.gasteMenu = gasteMenu

    # Get all guests with current or future booking - compare start date with current date
    def aktuelle_gaste(self):
        aktuelleGaste = []
        for obj in self.gasteMenu.get_GastList():
            ok = 0
            for obj1 in obj.get_reservierungen():
                if datetime.strptime( obj1.get_zeitraum()[0:13], "%Y:%m:%d %H" ) <= datetime.now() <= datetime.strptime(
                        obj1.get_zeitraum()[16:29], "%Y:%m:%d %H" ) :
                    ok = 1
            if ok == 1:
                aktuelleGaste.append( obj )
        return aktuelleGaste

    # Return all rooms which respect given condition
    def filltert_zimmer(self, preis, meerblick):
        filttertZimmern = []
        for obj in self.zimmerMenu.get_zimmerList():
            if float( obj.get_preis() ) <= preis and str( obj.get_meerblick() ) == meerblick:
                filttertZimmern.append( obj )
        return filttertZimmern

    # Print all free rooms for the current day
    def frei_zimmer_heute(self):
        occupiedRooms = []
        freeRooms = []
        # Create list with all rooms which have at least one booking
        for obj in self.gasteMenu.get_GastList():
            for obj1 in obj.get_reservierungen():
                if obj1 not in occupiedRooms and datetime.strptime( obj1.get_zeitraum()[0:10],
                                                                    "%Y:%m:%d" ) <= datetime.strptime(obj1.get_zeitraum()[16:26],"%Y:%m:%d") <= datetime.now():
                    occupiedRooms.append( obj1.get_zimmer() )
        # Print all rooms which do not belong to the list of occupied rooms
        for obj in self.zimmerMenu.get_zimmerList():
            if obj not in occupiedRooms:
                freeRooms.append( obj )
        return freeRooms
