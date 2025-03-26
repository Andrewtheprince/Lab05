import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def caricaCorsi(self):
        self.listaCorsi = self._model.getCorsi()
        for corso in self.listaCorsi:
            self._view._tendinaCorsi.controls.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))