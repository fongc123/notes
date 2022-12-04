"""
File: orange_peels.py

This file contains the dependencies for the age classification of dried orange peels.
"""

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader, Subset
from torchvision.io import read_image
import numpy as np
import pandas as pd
import random
import os

class OrangePeelsDataset(Dataset):
    def __init__(self, img_dir, class_size = None, transform = None, target_transform = None):
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform
        self.encoder = {6 : 0, 10 : 1, 15 : 2, 20 : 3}
        self.decoder = {v:k for k, v in self.encoder.items()}

        # store paths and labels in DataFrame
        data = { "image_path" : [], "label" : [] }
        for subdir in os.listdir(img_dir):
            files = [f for f in os.listdir(os.path.join(img_dir, subdir)) if f.startswith("IMG")]
            random.shuffle(files)
            for idx, file in enumerate(files):
                if class_size is not None:
                    if idx >= class_size:
                        break

                data["image_path"].append(os.path.join(img_dir, subdir, file))
                data["label"].append(int(subdir))

        self.annotations = pd.DataFrame(data).sample(frac = 1).reset_index(drop = True)

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, idx):
        image = read_image(self.annotations.iloc[idx, 0]).float()
        label = self.encoder[self.annotations.iloc[idx, 1]]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)

        return image, label