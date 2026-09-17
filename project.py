import networkx as nx
from networkx.algorithms import community
G = nx.DiGraph()

# Read from file
with open("data.txt", "r") as f:
    for line in f:
        u, v = line.strip().split()
        G.add_edge(u, v)

# PageRank
pagerank = nx.pagerank(G)

# Degree Centrality
degree = nx.degree_centrality(G)

print("=== PageRank (Influence Score) ===")
for user, score in sorted(pagerank.items(), key=lambda x: x[1], reverse=True):
    print(user, round(score, 3))

print("\n=== Degree Centrality ===")
for user, score in sorted(degree.items(), key=lambda x: x[1], reverse=True):
    print(user, round(score, 3))

print("\n Top Influencer:", max(pagerank, key=pagerank.get))

communities = list(community.greedy_modularity_communities(G))

print("\n=== Communities ===")
for i, comm in enumerate(communities):
    print(f"Community {i+1}:", list(comm))
bet = nx.betweenness_centrality(G)

top_bet = sorted(bet.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nTop Connectors (Bridges):")
for user, score in top_bet:
    print(user, round(score, 3))
