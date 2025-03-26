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
        return listaCorsi

if __name__ == "__main__":
    mydao = corsoDAO()
    mydao.getCorsi()