# Kaggle---Fisheries
Multiple Fish species detection 

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

First identify where the fish/es are in each image. To do this, I have adapted the Viola-Jones face recognition algorithm. By using the NoF category as a negative test set, and all other images as a positive test set.
