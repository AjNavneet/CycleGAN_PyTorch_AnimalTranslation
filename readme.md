# CycleGAN for Image To Image Translation - Wildlife

## Overview

Imagine receiving a self-portrait from the renowned Dutch Post-Impressionist painter Vincent van Gogh. Seems impossible, right? In recent years, Microsoft researchers have developed the CycleGAN model, specifically designed for unpaired image-to-image translation. This powerful model has a wide range of applications, from enhancing photographs to transforming seasons or styles. With CycleGAN, you can translate any image to another domain, regardless of whether they are paired.

---

## Aim
To build the CycleGAN Model in PyTorch for translating animal image to other domain irrespective of the pairing between two images.

---

## Data Description
The dataset includes images of horses in domain A and zebras in domain B, divided into train and test sets.

---

## Tech Stack
- Language: `Python`
- Libraries: `torch`, `torchvision`, `numpy`, `pillow`

---

## Approach
1. Introduction to CycleGAN
2. Introduction to ResNet
3. Loss function in CycleGAN
4. Building Model on PyTorch
5. Model training

---

## Modular Code Overview

1. **data:** Contains the horse2zebra dataset, split into train and test sets with domain A as Horse and domain B as Zebra.
2. **images:** Contains translated images from domain A to B.
3. **saved_model:** Placeholder for saving trained models.
4. **cyclegan.py:** The main script for training the CycleGAN model.
5. **datasets.py:** Contains code for data loading and preprocessing.
6. **models.py:** Defines the CycleGAN model architecture.
7. **utils.py:** Utility functions used in training.
8. **requirements.txt:** Lists all the required libraries with their respective versions. Install them using `pip install -r requirements.txt`.

---

