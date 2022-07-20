import os

import numpy as np
import torch
from torch.utils.data import Dataset
from torchvision import transforms
import cv2
import sys

transform = transforms.Compose([
    transforms.ToTensor()
])


class MyDataset(Dataset):
    def __init__(self, path, name):
        self.path = path
        self.name = name

    def __len__(self):
        return len(self.name)

    def __getitem__(self, index):
        segment_name = self.name[index]  # xx.img
        imgpath = os.path.join(self.path, 'img', segment_name)
        labelpath = os.path.join(self.path, 'label', segment_name.replace("png", "npy"))

        image = cv2.imread(imgpath, 0)
        label_value = np.load(labelpath)

        label = int(label_value) // 4

        label = torch.Tensor([label])

        return transform(image), label
