# Ford-Fulkerson algorithm in Python

class Graph:

    def __init__(self, graph):
        self.graph = graph  # original graph
        self.residual_graph = [[cell for cell in row] for row in graph]  # cloned graph
        self.latest_augmenting_path = [[0 for _ in row] for row in graph]  # empty graph with same dimension as graph
        self.current_flow = [[0 for _ in row] for row in graph]  # empty graph with same dimension as graph

    def ff_step(self, source, sink):
        """
        Perform a single flow augmenting iteration from source to sink. Update the latest augmenting path, the residual
        graph and the current flow by the maximum possible amount, according to the path found by BFS.
        @param source the source's vertex id
        @param sink the sink's vertex id
        @return the amount by which the flow has increased.
        """
        # TODO
        pass

    def ford_fulkerson(self, source, sink):
        """
        Execute the ford-fulkerson algorithm (i.e., repeated calls of ff_step())
        @param source the source's vertex id
        @param sink the sink's vertex id
        @return the max flow from source to sink
        """
        # TODO
        pass
