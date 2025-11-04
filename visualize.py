import matplotlib.pyplot as plt
import networkx as nx

def visualize_topology(G, highlight_path=None):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(7, 5))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1200, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{G[u][v]['weight']}" for u, v in G.edges()})
    if highlight_path:
        path_edges = list(zip(highlight_path, highlight_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
    plt.title("Network Topology Simulation")
    plt.show()
