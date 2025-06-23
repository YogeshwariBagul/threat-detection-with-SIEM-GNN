import pandas as pd
import networkx as nx
import torch
from torch_geometric.utils import from_networkx

# Load structured logs (CSV)
df = pd.read_csv("logs.csv")

# Initialize a directed graph
G = nx.DiGraph()

# Loop through logs and build graph
for _, row in df.iterrows():
    user = row.get("EventData.SubjectUserName", "UnknownUser")
    src_ip = row.get("EventData.IpAddress", "0.0.0.0")
    logon_id = row.get("EventData.TargetLogonId", "None")
    event_id = row.get("EventID", "0")

    # Add nodes
    G.add_node(user, type="User")
    G.add_node(src_ip, type="IP")
    G.add_node(logon_id, type="LogonID")
    G.add_node(str(event_id), type="Event")

    # Add edges
    G.add_edge(user, src_ip, relation="logged_from")
    G.add_edge(user, logon_id, relation="session")
    G.add_edge(user, str(event_id), relation="triggered_event")

# Convert NetworkX graph to PyTorch Geometric Data
pyg_graph = from_networkx(G)

# Save the graph for GNN processing
torch.save(pyg_graph, "windows_graph.pt")
print("Graph saved as 'windows_graph.pt'!")
