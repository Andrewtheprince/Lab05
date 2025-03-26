from database.DB_connect import get_connection
import mysql.connector

class studenteDAO:

    def __init__(self):
        pass

    def getStudentiCorso(self, corso):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ select *
                    from iscrizione i, studente s
                    where i.codins = %s and i.matricola = s.matricola """
        cursor.execute(query, (corso,))
        listaStudenti = []
        for row in cursor:
            listaStudenti.append(row)
        cursor.close()
        return listaStudenti

    def getStudente(self, matricola):
        #terminare qua quello che serve per trovare lo studente dalla matricola
        pass