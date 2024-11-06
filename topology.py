import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import gudhi as gd


# Step 1: Create a graph with weighted edges
def create_weighted_graph():
    G = nx.Graph()

    # Add nodes
    G.add_nodes_from([1, 2, 3, 4, 5])

    # Add edges with weights
    G.add_edge(1, 2, weight=0.1)
    G.add_edge(1, 3, weight=0.4)
    G.add_edge(2, 3, weight=0.3)
    G.add_edge(2, 4, weight=0.6)
    G.add_edge(3, 4, weight=0.7)
    G.add_edge(4, 5, weight=0.2)

    return G


# Step 2: Build filtration based on edge weights
def filtration_by_weights(G):
    edges = list(G.edges(data=True))  # Get edges with weights
    edges.sort(key=lambda x: x[2]['weight'])  # Sort edges by weight

    # Build the filtration by adding edges in increasing order of weight
    filtration = gd.SimplexTree()

    # Add vertices first
    for node in G.nodes:
        filtration.insert([node])  # Insert vertices
        filtration.assign_filtration([node], 0)  # Set filtration value to 0 for vertices

    # Add edges in order of increasing weight
    for edge in edges:
        filtration.insert([edge[0], edge[1]])  # Insert edge
        filtration.assign_filtration([edge[0], edge[1]], edge[2]['weight'])  # Assign filtration time

        # Check if adding higher-dimensional simplices is possible (cliques)
        cliques = list(nx.find_cliques(G.subgraph([edge[0], edge[1]])))
        for clique in cliques:
            if len(clique) > 2:  # Add cliques with more than 2 vertices
                filtration.insert(clique)
                filtration.assign_filtration(clique, edge[2]['weight'])

    return filtration


# Step 3: Compute persistence
def compute_persistence(filtration):
    persistence = filtration.persistence()
    return persistence


# Step 4: Plot the persistence diagram
def plot_persistence_diagram(filtration):
    gd.plot_persistence_diagram(filtration.persistence())
    plt.show()


# Main execution
if __name__ == "__main__":
    # Create a weighted graph
    G = create_weighted_graph()

    # Build the filtration by edge weights
    filtration = filtration_by_weights(G)

    # Compute persistence of the filtration
    persistence = compute_persistence(filtration)

    # Print persistence intervals
    print("Persistence intervals:")
    for interval in persistence:
        print(interval)

    # Plot the persistence diagram
    plot_persistence_diagram(filtration)
