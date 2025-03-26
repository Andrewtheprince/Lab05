import database.corso_DAO as cd
from model.corso import Corso

class Model:
    def __init__(self):
        self.CorsoDao = cd.corsoDAO()

    def getCorsi(self):
        listaCorsi = self.CorsoDao.getCorsi()
        listaCorsiAggiornata =[]
        for row in listaCorsi:
            corso = Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
            listaCorsiAggiornata.append(corso)
        return listaCorsiAggiornata