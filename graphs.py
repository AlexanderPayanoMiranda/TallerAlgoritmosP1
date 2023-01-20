import networkx as nx

graph = nx.Graph()

graph.add_node("A")
graph.add_node("E")
graph.add_node("I")
graph.add_edge("A", "E")
graph.add_edge("E", "I")
graph.add_edge("I", "O")

print(graph.nodes)
print(graph.edges)
