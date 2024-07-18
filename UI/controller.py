import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []
        #-------
        # aggiunti dal programmatore
        self._choiceYear = None
        self._choiceForma = None

    def handle_graph(self, e):
        self._view._txt_result.controls.clear()
        self._model.buildGraph()

        nN, nE = self._model.getGraphDetails()
        self._view._txt_result.controls.append(
            ft.Text(f"Grafo correttamente creato"))
        self._view._txt_result.controls.append(
            ft.Text(f"Num nodi = {nN}"))
        self._view._txt_result.controls.append(
            ft.Text(f"Num archi = {nE}"))

        self._view.update_page()

    def handle_path(self, e):
        pass

    def fillDDYear(self):
        self._listYear = self._model.getAllYears()
        for y in self._listYear:
            self._view.ddyear.options.append(
                ft.dropdown.Option(data=y,
                                   on_click=self.readDDYear,
                                   text=y
                                   ))

    def readDDYear(self, e):
        year = e.control.data
        if year is None:
            self._view._txt_result.controls.append("Non è stato selezionato nessun anno")
            self._view.update_page()
        else:
            self._choiceYear = year


    def fillDDForma(self):
        self._listShape = self._model.getAllForme()
        for s in self._listShape:
            self._view.ddshape.options.append(
                ft.dropdown.Option(data=s,
                                   on_click=self.readDDYear,
                                   text=s
                                   ))

    def readDDForma(self, e):
        forma = e.control.data
        if forma is None:
            self._view._txt_result.controls.append("Non è stato selezionata nessuna forma")
            self._view.update_page()
        else:
            self._choiceForma = forma