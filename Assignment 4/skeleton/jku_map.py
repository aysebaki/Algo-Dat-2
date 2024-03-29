import sys
from typing import List, Dict
from graph import Graph
from vertex import Vertex
from step import Step


class JKUMap(Graph):
    # visitedNodes = []
    # distances = []

    def __init__(self):
        super().__init__()
        v_spar = self.add_vertex("Spar")
        v_lit = self.add_vertex("LIT")
        v_porter = self.add_vertex("Porter")
        v_open_lab = self.add_vertex("Open Lab")
        v_bank = self.add_vertex("Bank")
        v_khg = self.add_vertex("KHG")
        v_chat = self.add_vertex("Chat")
        v_parking = self.add_vertex("Parking")
        v_bella_casa = self.add_vertex("Bella Casa")
        v_lib = self.add_vertex("Library")
        v_lui = self.add_vertex("LUI")
        v_teichwerk = self.add_vertex("Teichwerk")
        v_sp1 = self.add_vertex("SP1")
        v_sp3 = self.add_vertex("SP3")
        v_castle = self.add_vertex("Castle")
        v_papaya = self.add_vertex("Papaya")
        v_jkh = self.add_vertex("JKH")

        self.add_edge(v_jkh.name, v_papaya.name, 80)
        self.add_edge(v_papaya.name, v_castle.name, 85)
        self.add_edge(v_sp3.name, v_sp1.name, 130)
        self.add_edge(v_sp1.name, v_lui.name, 175)
        self.add_edge(v_sp1.name, v_parking.name, 240)
        self.add_edge(v_parking.name, v_bella_casa.name, 145)
        self.add_edge(v_parking.name, v_khg.name, 190)
        self.add_edge(v_khg.name, v_bank.name, 150)
        self.add_edge(v_khg.name, v_spar.name, 165)
        self.add_edge(v_spar.name, v_lit.name, 50)
        self.add_edge(v_spar.name, v_porter.name, 103)
        self.add_edge(v_lit.name, v_porter.name, 80)
        self.add_edge(v_porter.name, v_open_lab.name, 70)
        self.add_edge(v_porter.name, v_bank.name, 100)
        self.add_edge(v_chat.name, v_bank.name, 115)
        self.add_edge(v_chat.name, v_lib.name, 160)
        self.add_edge(v_chat.name, v_lui.name, 240)
        self.add_edge(v_lui.name, v_teichwerk.name, 135)
        self.add_edge(v_lui.name, v_lib.name, 90)

    def get_shortest_path_from_to(self, from_vertex: Vertex, to_vertex: Vertex) -> List[Step]:
        """
        This method determines the shortest path between two POIs "from_vertex" and "to_vertex".
        It returns the list of intermediate steps of the route that have been found
        using the dijkstra algorithm.

        :param from_vertex: Start vertex
        :param to_vertex:   Destination vertex
        :return:
           The path, with all intermediate steps, returned as an list. This list
           sequentially contains each vertex along the shortest path, together with
           the already covered distance (see example on the assignment sheet).
           Returns None if there is no path between the two given vertices.
        :raises ValueError: If from_vertex or to_vertex is None, or if from_vertex equals to_vertex
        """
        if from_vertex is None or to_vertex is None or from_vertex == to_vertex:
            raise ValueError("Invalid vertices")

            # Initialize data structures
        visited_set = set()
        distances = {vertex: float('inf') for vertex in self.vertices}
        paths = {vertex: None for vertex in self.vertices}

        # Set the distance of the starting vertex to 0
        distances[from_vertex] = 0

        # Call the _dijkstra method
        self._dijkstra(from_vertex, visited_set, distances, paths)

        # Construct the path from the paths dictionary
        path = [Step(to_vertex, distances[to_vertex])]
        current_vertex = to_vertex
        while current_vertex != from_vertex:
            previous_vertex = paths[current_vertex]
            path.insert(0, Step(previous_vertex, distances[previous_vertex]))
            current_vertex = previous_vertex

        return path

    def get_shortest_distances_from(self, from_vertex: Vertex):
        """
        This method determines the amount of "steps" needed on the shortest paths
        from a given "from" vertex to all other vertices.
        The number of steps (or -1 if no path exists) to each vertex is returned
        as a dictionary, using the vertex name as key and the distance as value.
        E.g., the "from" vertex has a step count of 0 to itself and 1 to all adjacent vertices.

        :param from_vertex: start vertex
        :return:
          A map containing the number of steps (or -1 if no path exists) on the
          shortest path to each vertex, using the vertex name as key and the distance as value.
        :raises ValueError: If from_vertex is None.
        """
        if from_vertex is None:
            raise ValueError("Invalid starting vertex")

            # Initialize data structures
        visited_set = set()
        distances = {vertex.name: float('inf') for vertex in self.vertices}
        paths = {vertex: None for vertex in self.vertices}

        # Set the distance of the starting vertex to 0
        distances[from_vertex.name] = 0

        # Call the _dijkstra method
        self._dijkstra(from_vertex, visited_set, distances, paths)

        return distances

    # This method is not mandatory, but a recommendation by us
    def _dijkstra(self, cur: Vertex, visited_set: set, distances: Dict[Vertex, int], paths: Dict[Vertex, Vertex]):
        """
        This method is expected to be called with correctly initialized data structures and recursively calls itself.

        :param cur: Current vertex being processed
        :param visited_set: Set which stores already visited vertices.
        :param distances: Dict (nVertices entries) which stores the min. distance to each vertex.
        :param paths: Dict (nVertices entries) which stores the shortest path to each vertex.
        """
        visited_set.add(cur)

        for edge in self.edges:
            if edge.first == cur and edge.second not in visited_set:
                new_distance = distances[cur] + edge.weight
                if new_distance < distances[edge.second]:
                    distances[edge.second] = new_distance
                    paths[edge.second] = cur

            elif edge.second == cur and edge.first not in visited_set:
                new_distance = distances[cur] + edge.weight
                if new_distance < distances[edge.first]:
                    distances[edge.first] = new_distance
                    paths[edge.first] = cur

        # Find the next vertex with the smallest distance
        next_vertex = min(
            (vertex for vertex in self.vertices if vertex not in visited_set),
            key=lambda vertex: distances[vertex]
        )

        if distances[next_vertex] != float('inf'):
            self._dijkstra(next_vertex, visited_set, distances, paths)
