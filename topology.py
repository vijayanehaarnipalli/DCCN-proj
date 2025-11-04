import networkx as nx

class Topology:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, name):
        self.graph.add_node(name)

    def add_link(self, n1, n2, weight=1):
        self.graph.add_edge(n1, n2, weight=weight)

    def remove_node(self, name):
        if name in self.graph:
            self.graph.remove_node(name)

    def remove_link(self, n1, n2):
        if self.graph.has_edge(n1, n2):
            self.graph.remove_edge(n1, n2)

    def shortest_path(self, src, dst):
        return nx.shortest_path(self.graph, source=src, target=dst, weight="weight")

    def nodes(self):
        return list(self.graph.nodes())

    def links(self):
        return list(self.graph.edges())
