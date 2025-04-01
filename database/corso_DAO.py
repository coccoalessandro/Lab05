# Add whatever it is needed to interface with the DB Table corso
import mysql

from database.DB_connect import get_connection


class IscrittiDao:
    def __init__(self):
        pass

    def getCorsi(self):
        cnx = get_connection()
        cursor = cnx.cursor()

        query = "SELECT * FROM corso"
        cursor.execute(query)

        listaCorsi = []

        for row in cursor:
            listaCorsi.append(row)

        return listaCorsi

        cnx.close()

    def getStudenti(self):
        cnx = get_connection()
        cursor = cnx.cursor()

        query = "SELECT * FROM studente"
        cursor.execute(query)

        listaStudenti = []

        for row in cursor:
            listaStudenti.append(row)

        return listaStudenti

        cnx.close()

    def getIscritti(self):
        cnx = get_connection()
        cursor = cnx.cursor()

        query = "SELECT * FROM iscrizione"
        cursor.execute(query)

        listaIscritti = []

        for row in cursor:
            listaIscritti.append(row)

        return listaIscritti

        cnx.close()

if __name__ == '__main__':
    mydao = IscrittiDao()
    print(mydao.getCorsi())