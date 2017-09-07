# Kaggle: Fisheries multi-species fish detection 
# (Image recognition problem)

The latest 3-fold cross-validation weights are 'bbox_weights0.h5' - training on bounding boxes and whole images with the relabelled images (using the relabelling scripts). bbox of test data is only 0.70 score or higher.


Kaggle competition to assign a probability that an image contains one of eight catagories:

1. ALB
2. BET
3. DOL
4. LAG
5. NoF (No fish)
6. Other - (unidentified species)
7. SHARK
8. YFT

![alt tag](https://raw.githubusercontent.com/GlastonburyC/Kaggle---Fisheries/master/Screen%20Shot%202016-12-26%20at%2002.08.52.png?token=AEA_SyfjdeHYyRLMjwSuwSXrwGt_O11nks5YaoSnwA%3D%3D)

![alt tag](https://raw.githubusercontent.com/GlastonburyC/Kaggle---Fisheries/master/Screen%20Shot%202016-12-26%20at%2001.52.06.png?token=AEA_SzSyTAH5s0Gm4-bBFz1ZKHuf-jaoks5YaoRNwA%3D%3D)


![alt tag](https://raw.githubusercontent.com/GlastonburyC/Kaggle---Fisheries/master/Screen%20Shot%202016-12-26%20at%2002.09.05.png?token=AEA_S9Rb2nN05gvJ6X2Aya32oTF3A1ITks5YaoUAwA%3D%3D)

Best so far, 1000 augmentations of all cropped images and all original images scaled to 299 x 299.
Mean of crops from each image performs better than maximum probability.

