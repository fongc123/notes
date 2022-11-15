from torch.utils.data import Dataset, DataLoader, Subset
from torchvision.io import read_image
import torchvision.transforms as transforms
import pandas as pd
import os

class CustomDataset(Dataset):
    def __init__(self, root_dir, transform = None):
        self.root_dir = root_dir
        self.transform = transform

        data = { "image_path" : [] }
        for sub_dir in os.listdir(root_dir):
            for sub_sub_dir in os.listdir(os.path.join(root_dir, sub_dir)):
                for file in os.listdir(os.path.join(root_dir, sub_dir, sub_sub_dir)):
                    data["image_path"].append(os.path.join(root_dir, sub_dir, sub_sub_dir, file))

        self.annotations = pd.DataFrame(data).sample(frac = 1).reset_index(drop = True)

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, idx):
        image = read_image(self.annotations.iloc[idx ,0])
        if self.transform:
            image = self.transform(image)
        return image