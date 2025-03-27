import mysql.connector
import database.DB_connect as db

class corsoDAO:

    def __init__(self):
        pass

    def getCorsi(self):

        cnx = db.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query="""SELECT * FROM corso"""
        cursor.execute(query)
        listaCorsi =[]
        for row in cursor:
            listaCorsi.append(row)
        cursor.close()
        cnx.close()
        return listaCorsi

    def corsiStudente(self, matricola):
        cnx = db.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * 
                    FROM corso c, iscrizione i
                    WHERE i.matricola = %s and c.codins = i.codins"""
        cursor.execute(query, (matricola,))
        listaCorsi = []
        for row in cursor:
            listaCorsi.append(row)
        cursor.close()
        cnx.close()
        return listaCorsi

if __name__ == "__main__":
    mydao = corsoDAO()
    mydao.getCorsi()