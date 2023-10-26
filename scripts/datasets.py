# Import necessary libraries
import glob
import random
import os
from torch.utils.data import Dataset
from PIL import Image
import torchvision.transforms as transforms

# Define a function to convert images to RGB mode
def to_rgb(image):
    rgb_image = Image.new("RGB", image.size)
    rgb_image.paste(image)
    return rgb_image

# Define a custom dataset class called ImageDataset
class ImageDataset(Dataset):
    def __init__(self, root, transforms_=None, unaligned=False, mode="train"):
        # Initialize the dataset
        self.transform = transforms.Compose(transforms_)
        self.unaligned = unaligned

        # Create lists of image file paths for dataset A and B
        self.files_A = sorted(glob.glob(os.path.join(root, "%s/A" % mode) + "/*.*"))
        self.files_B = sorted(glob.glob(os.path.join(root, "%s/B" % mode) + "/*.*"))

    def __getitem__(self, index):
        # Get and process images for a given index
        image_A = Image.open(self.files_A[index % len(self.files_A)])

        if self.unaligned:
            image_B = Image.open(self.files_B[random.randint(0, len(self.files_B) - 1)])
        else:
            image_B = Image.open(self.files_B[index % len(self.files_B)])

        # Convert grayscale images to RGB
        if image_A.mode != "RGB":
            image_A = to_rgb(image_A)
        if image_B.mode != "RGB":
            image_B = to_rgb(image_B)

        # Apply specified transformations to both images
        item_A = self.transform(image_A)
        item_B = self.transform(image_B)

        # Return a dictionary with processed images
        return {"A": item_A, "B": item_B}

    def __len__(self):
        # Return the maximum length between the two dataset directories
        return max(len(self.files_A), len(self.files_B))
