# Kaggle: Fisheries multi-species fish detection 
# (Image recognition problem)

The latest k-fold cross-validation weights are in train_relabelled/ and new_labels/. They are 45 epoch runs with 960x640 bbox predictiond using high confidence assignment IOU = 0.70

weights0,1,2,3.h5


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

The approach I have currently implemented simply classifies the whole image (resized to 299 x 299), using a transfer learning approach. The convolutional neural network (CNN) I'm using is the Inception V3 CNN trained on ImageNet. As training a deep CNN like Inception V3 is expensive, I am using transfer learning, in which only the top layer is removed and replaced with a dense softmax layer. The softmax function allows the output of normalised probabilities (summing to one) and is suitable for cases when labels are mutually exclusive. In addition to this, I am also using image augmentation to make the CNN more robust to scaling, normalisation, shifts, rotations and shear. 

Further work will involved splitting not just into training and validation, but two validation sets, or k-fold cross validation.

Use: https://github.com/facebook/fb.resnet.torch/tree/master/pretrained to extract fishes from whole images


![alt tag](https://raw.githubusercontent.com/GlastonburyC/Kaggle---Fisheries/master/Screen%20Shot%202016-12-26%20at%2002.08.52.png?token=AEA_SyfjdeHYyRLMjwSuwSXrwGt_O11nks5YaoSnwA%3D%3D)

![alt tag](https://raw.githubusercontent.com/GlastonburyC/Kaggle---Fisheries/master/Screen%20Shot%202016-12-26%20at%2001.52.06.png?token=AEA_SzSyTAH5s0Gm4-bBFz1ZKHuf-jaoks5YaoRNwA%3D%3D)


![alt tag](https://raw.githubusercontent.com/GlastonburyC/Kaggle---Fisheries/master/Screen%20Shot%202016-12-26%20at%2002.09.05.png?token=AEA_S9Rb2nN05gvJ6X2Aya32oTF3A1ITks5YaoUAwA%3D%3D)

Best so far, 1000 augmentations of all cropped images and all original images scaled to 299 x 299.
Mean of crops from each image performs better than maximum probability.

