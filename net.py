from torch import nn

class Net(nn.Module):
 
  def __init__(self, input_dim, hidden_dim, n_layers):
    super().__init__()
    self.input_dim = input_dim
    self.hidden_dim = hidden_dim
    self.n_layers = n_layers
 
    self.input_layer = nn.Sequential(
        nn.BatchNorm1d(input_dim),
        nn.Linear(input_dim, hidden_dim),
        nn.ReLU(inplace=True)
    )
 
    middle = []
    for _ in range(n_layers):
      middle.append(nn.BatchNorm1d(hidden_dim),)
      middle.append(nn.Linear(hidden_dim, hidden_dim))
      middle.append(nn.ReLU(inplace=True))
 
    self.middle_layers = nn.Sequential(*middle)
 
    self.output_layer = nn.Linear(hidden_dim, 9)
 
 
  def forward(self, x):
    x = self.input_layer(x)
    x = self.middle_layers(x)
    x = self.output_layer(x)
    return x