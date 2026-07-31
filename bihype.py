import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class PositionalEmbedding(nn.Module):
    def __init__(self, d_model, max_len=64):
        super(PositionalEmbedding, self).__init__()
        self.d_model = d_model
        self.max_len = max_len
        self.position = torch.arange(max_len)

        bits = torch.arange(
            int(torch.log2(torch.tensor(float(max_len))).item()) - 1,
            -1,
            -1,
            dtype=torch.long
        )

        binary_pos = (
            (self.position[:, None] & (1 << bits)) > 0
        ).float() 
        self.register_buffer("binary_pos", binary_pos)                                                # (128,7)

        # Calculate the temporal distance between tokens and normalize it to the range [-1, 1]
        dist = self.position[None, :] - self.position[:, None]
        mask = ~torch.eye(max_len, dtype=torch.bool)
        dist = dist[mask].view(max_len, max_len - 1).float()
        dist = dist / (dist.size(-1))
        self.register_buffer("dist", dist)

        # Relative feature embedding module
        self.relative_compression = nn.Sequential(
            nn.Linear(
                max_len - 1,
                d_model - int(math.log2(max_len))
            ),
            nn.ReLU()
        )   

        # self.alpha = nn.Parameter(torch.tensor(0.6))
        self.absolute_compression = nn.Linear(int(math.log2(max_len)), int(math.log2(max_len)))
        self.gating = nn.Parameter(torch.tensor(0.0))

    def forward(self, x):
        gate = torch.sigmoid(self.gating)
        relative_out = self.relative_compression(self.dist)
        absolute_out = self.absolute_compression(self.binary_pos)
        pe = torch.cat([(1-gate) * relative_out, gate * absolute_out], dim=-1)    # (256, 9+7=16)
        
        # Return full, relative, absolute
        return pe.unsqueeze(0)