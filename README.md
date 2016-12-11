# Kaggle: Fisheries multi-species fish detection 
# (Image recognition problem)

Kaggle competition to assign a probability that an image contains one of eight catagories:

1. ALB
2. BET
3. DOL
4. LAG
5. NoF (No fish)
6. Other - (unidentified species)
7. SHARK
8. YFT

# Approach:

First: identify where the fish/es are in each image. To do this, I adapted the Viola-Jones face recognition algorithm. By using the NoF category as a negative test set, and all other images as a positive test set.

This apporach failed to identify bounding boxes around fish, possibly because the signal to noise ratio (SNR) in each image is so high. Another apprach to test would be to apply a convolutional neural network such as DetectNet or OverFeat. The objective here is to minimise noise, as classifying the fish should be easier than classifying the entire image with many non-useful features.

The approach I have currently implemented simply classifies the whole image (resized to 299 x 299), using a transfer learning approach. The convolutional neural network (CNN) I'm using is the Inception V3 CNN trained on ImageNet. As training a deep CNN like Inception V3 is expensive, I am using trasnfer learning, in which only the top layer is removed and replaced with a dense softmax layer. The softmax function allows the output of normalised probabilities (summing to one) and is suitable for cases when labels are mutually exclusive. In addition to this, I am also using image augmentation to make the CNN more robust to scaling, normalisation, shifts, rotations and shear. 

Further work will involved splitting not just into training and validation, but two validation sets, or k-fold cross validation.
