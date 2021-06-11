class Reservierung:

    def __init__(self):
        pass

    #Setters
    def set_zimmer(self, zimmer):
        self.zimmer = zimmer
    def set_zeitraum(self,zeitraum):
        self.zeitraum = zeitraum
    def set_gastenummer(self, gastenummer):
        self.gastenummer = gastenummer

    #Getters
    def get_zimmer(self):
        return self.zimmer
    def get_zeitraum(self):
        return self.zeitraum
    def get_gastenummer(self):
        return self.gastenummer