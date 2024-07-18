import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._allYears = DAO.getAllYears()
        self._allForme = DAO.getAllForme()
        self._allStates = DAO.getAllStates()
        self._idMap = {}

        self._grafo = nx.Graph()

        self._


    def buildGraph(self, forma, anno):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._allStates)

        for s in self._allStates:
            self._idMap[s.id] = s

        allEdges = DAO.getAllNeighbours(self._idMap)
        allPesi = DAO.getAllPeso(self._idMap, forma, anno)

        for e in allEdges:
            self._grafo.add_edge(e[0], e[1], weight=allPesi)

        # allPesi = DAO.getAllPeso(self._idMap, forma, anno)
        # for e in allEdges:
        #     for a in allPesi:
        #         if e[0]
        #         self._grafo[e[0]][e[1]]["weight"]





    def getAllYears(self):
        return self._allYears

    def getAllForme(self):
        return self._allForme

    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)



