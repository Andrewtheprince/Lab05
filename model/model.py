import database.corso_DAO as cd
from model.corso import Corso
from model.studente import Studente
import database.studente_DAO as sd

class Model:
    def __init__(self):
        self.corsoDao = cd.corsoDAO()
        self.studenteDao = sd.studenteDAO()

    def getCorsi(self):
        listaCorsi = self.corsoDao.getCorsi()
        listaCorsiAggiornata =[]
        for row in listaCorsi:
            corso = Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
            listaCorsiAggiornata.append(corso)
        return listaCorsiAggiornata

    def getStudenti(self, corsoSelezionato):
        listaStudenti = self.studenteDao.getStudentiCorso(corsoSelezionato)
        listaStudentiAggiornata = []
        for row in listaStudenti:
            if "cds" in row:
                studente = Studente(row["matricola"], row["cognome"], row["nome"], row["cds"])
            else:
                studente = Studente(row["matricola"], row["cognome"], row["nome"], "Non definito")
            listaStudentiAggiornata.append(studente)
        return listaStudentiAggiornata

    def getStudente(self, matricola):
        studente = self.studenteDao.getStudente(matricola)
        if studente == "None":
            return "None"
        studente1 = Studente(studente[0], studente[1], studente[2], "Non definito")
        return studente1

    def corsiStudente(self, matricola):
        listaCorsi = self.corsoDao.corsiStudente(matricola)
        listaCorsiAggiornata = []
        for row in listaCorsi:
            corso = Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
            listaCorsiAggiornata.append(corso)
        return listaCorsiAggiornata

    def iscrivi(self, corsoSelezionato, matricola):
        self.studenteDao.iscrivi(corsoSelezionato, matricola)

