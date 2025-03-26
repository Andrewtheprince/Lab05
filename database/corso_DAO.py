import mysql.connector

class corsoDAO:

    def __init__(self):
        pass

    def getCorsi(self):
        cnx=mysql.connector.connect(user="root",
                                    password="root",
                                    host="127.0.0.1",
                                    database="iscritticorsi")
        cursor = cnx.cursor(dictionary=True)
        query="""SELECT (codins, crediti, nome, pd) FROM corso"""
        cursor.execute(query)
        listaCorsi =[]
        for row in cursor:
            listaCorsi.append(row)
        cursor.close()
        return listaCorsi

if __name__ == "__main__":
    mydao = corsoDAO()
    mydao.getCorsi()