import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch_geometric.nn import GCNConv
from torch_geometric.data import Data

# Define the GNN model
class ThreatDetectionGNN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):  # Fixed __init__
        super(ThreatDetectionGNN, self).__init__()
        self.conv1 = GCNConv(input_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, output_dim)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = F.dropout(x, training=self.training)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

# Check for GPU availability
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Sample graph data
num_nodes = 100
num_features = 128
pyg_graph = Data(
    x=torch.randn(num_nodes, num_features),
    edge_index=torch.randint(0, num_nodes, (2, 200)),
    y=torch.randint(0, 2, (num_nodes,))
)
labels = pyg_graph.y

# Move to device
pyg_graph = pyg_graph.to(device)
labels = labels.to(device)

# Initialize model, optimizer, and loss function
model = ThreatDetectionGNN(input_dim=num_features, hidden_dim=64, output_dim=2).to(device)
optimizer = optim.Adam(model.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

# Training loop
for epoch in range(50):
    model.train()
    optimizer.zero_grad()
    
    output = model(pyg_graph.x, pyg_graph.edge_index)
    loss = criterion(output, labels)
    
    loss.backward()
    optimizer.step()
    
    # Print loss and accuracy every 5 epochs
    if epoch % 5 == 0:
        with torch.no_grad():
            _, preds = output.max(dim=1)
            accuracy = (preds == labels).float().mean()
        print(f"Epoch {epoch}: Loss = {loss.item():.4f}, Accuracy = {accuracy:.4f}")
torch.save(model.state_dict(), "gnn_model.pth")