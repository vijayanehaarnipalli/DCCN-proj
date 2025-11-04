from topology import Topology
from visualize import visualize_topology
from simulation import simulate_transfer

def main():
    topo = Topology()

    # Build a sample mesh topology
    for n in ["A", "B", "C", "D"]:
        topo.add_node(n)
    topo.add_link("A", "B", 10)
    topo.add_link("A", "C", 5)
    topo.add_link("B", "C", 2)
    topo.add_link("B", "D", 5)
    topo.add_link("C", "D", 10)

    print("Nodes:", topo.nodes())
    print("Links:", topo.links())

    # Simulate data transfer
    result = simulate_transfer(topo, "A", "D")
    print("Simulation Result:", result)

    # Visualize network and highlight path
    visualize_topology(topo.graph, highlight_path=topo.shortest_path("A", "D"))

if __name__ == "__main__":
    main()
