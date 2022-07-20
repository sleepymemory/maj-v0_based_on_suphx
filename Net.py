#!/usr/bin/env python
# coding: utf-8


import torch
from torch import nn
from torch.nn import functional as F
import copy


class Conv1_Block_st(nn.Module):
    def __init__(self):
        super(Conv1_Block_st, self).__init__()
        self.layer = nn.Sequential(
            nn.Conv1d(431, 300, 3, 1, padding=1, padding_mode='zeros', bias=False),
            nn.BatchNorm1d(300),
            nn.LeakyReLU(0.2),

        )

    def forward(self, x):
        return self.layer(x)


class Conv1_Block(nn.Module):
    def __init__(self):
        super(Conv1_Block, self).__init__()
        self.layer = nn.Sequential(
            nn.Conv1d(300, 300, 3, 1, padding=1, padding_mode='zeros', bias=False),
            nn.BatchNorm1d(300),
            nn.LeakyReLU(0.2),
            nn.Conv1d(300, 300, 3, 1, padding=1, padding_mode='zeros', bias=False),
            nn.BatchNorm1d(300),
            nn.LeakyReLU(0.2),
        )

    def forward(self, x):
        return x + self.layer(x)


class Conv1_Block_end(nn.Module):
    def __init__(self):
        super(Conv1_Block_end, self).__init__()
        self.layer = nn.Sequential(
            nn.Conv1d(300, 1, 1, 1, padding=0, padding_mode='zeros', bias=False),
            nn.BatchNorm1d(1),
        )

    def forward(self, x):
        return self.layer(x)


def clones(module, N):
    return nn.ModuleList([copy.deepcopy(module) for _ in range(N)])


class myNet1(nn.Module):
    def __init__(self):
        super().__init__()
        self.st_layer = Conv1_Block_st()  # 2

        self.mid_layer = clones(Conv1_Block(), 70)
        self.drops = clones(nn.Dropout(0.1), 14)

        self.end_layer = Conv1_Block_end()

    def forward(self, x):
        x = self.st_layer(x)
        for i, layer in enumerate(self.mid_layer):
            x = layer(x)
            if i % 5 == 4:
                x = self.drops[i // 5](x)

        out = self.end_layer(x)
        return out.squeeze(1)
