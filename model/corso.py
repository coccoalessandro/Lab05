from flet.core import row

from database.corso_DAO import IscrittiDao

class Corso:
    def __init__(self, codins, crediti, nome, pd):
        self.codins = codins
        self.crediti = crediti
        self.nome = nome
        self.pd = pd

    def getCorsi(self):
        corsi = []

        mydao = IscrittiDao()

        for row in mydao.getCorsi():
            c = Corso(row[0], row[1], row[2], row[3])
            corsi.append(c)
        print(corsi)




