from database.DAO import DAO
import networkx as nx
from model.connessione import Connessione

class Model:
    def __init__(self):
        self._objects = [
        ]

    def objects(self):
        self._objects =[]
        self.get_objects()
        self._objects_dict = {}

        for o in self._objects_list:
            self._objects_dict[o.object_id] = o

        #grafico sempplice e pesato, non diretto
        self._grafo = nx.Graph()

    def get_objects(self):
        self._objects_list = DAO.read_objects()

    def buildGrafo(self):
        # nodi
        self._grafo.add_nodes_from(self._objects_list)
        #grafi
        # modo 1 (tempo lunghissimo)
        '''
        for u in self._objects_list:
            for v in self._objects_list:
                DAO.readEdges(u, v) # da scrivere '''
        # modo 2

        connessioni = DAO.readConnessioni(self._objects_dict)

        for c in connessioni:
            self._grafo.add_edge(c.o1, c.o2)