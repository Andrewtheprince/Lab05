import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def caricaCorsi(self):
        self.listaCorsi = self._model.getCorsi()
        for corso in self.listaCorsi:
            self._view._tendinaCorsi.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))

    def cercaIscritti(self, e):
        if self._view._tendinaCorsi.value == None:
            self._view.create_alert("Selezionare un corso!")
            return
        corsoSelezionato = self._view._tendinaCorsi.value
        studentiCorso = self._model.getStudenti(corsoSelezionato)
        for studente in studentiCorso:
            self._view._txtOut.controls.append(ft.Text(studente.__str__()))
        self._view.update_page()
