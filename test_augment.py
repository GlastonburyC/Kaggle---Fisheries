# highest score, shears 0.1, rotation 180, nbr_augmentation = 100000

from keras.models import load_model
import os
from keras.preprocessing.image import ImageDataGenerator
import numpy as np

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

img_width = 299
img_height = 299
batch_size = 32
nbr_test_samples = 2104*5
nbr_augmentation = 100

FishNames = ['ALB_fish', 'BET_fish', 'DOL_fish', 'LAG_fish', 'NoF_fish', 'OTHER_fish', 'SHARK_fish', 'YFT_fish']

root_path = '/home/craig/Desktop/tensorbox/'
weights_path = '/home/craig/Desktop/tensorbox/new_labels/fishbbox_plus_whole.weights.h5'

test_data_dir = os.path.join(root_path,'test_stg1_960x640/')

# test data generator for prediction
test_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.1,
        zoom_range=0.1,
        rotation_range=180,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip=True,
        vertical_flip=True)

print('Loading model and weights from training process ...')
InceptionV3_model = load_model(weights_path)
random_seed=[]
for idx in range(nbr_augmentation):
    print('{}th augmentation for testing ...'.format(idx))
    if idx == 0:
       random_seed.append(np.random.random_integers(0, 1000000))
    else:
        random_seed.insert(idx,np.random.random_integers(0, 1000000))    
    test_generator = test_datagen.flow_from_directory(
            test_data_dir,
            target_size=(img_width, img_height),
            batch_size=batch_size,
            shuffle = False, # Important !!!
            seed = random_seed[idx],
            classes = None,
            class_mode = None)
    test_image_list = test_generator.filenames
        #print('image_list: {}'.format(test_image_list[:10]))
    print('Begin to predict for testing data ...')
    if idx == 0:
        predictions = InceptionV3_model.predict_generator(test_generator, nbr_test_samples)
    else:
        predictions += InceptionV3_model.predict_generator(test_generator, nbr_test_samples)

predictions /= nbr_augmentation

print('Begin to write submission file ..')
seed_submit=open(os.path.join(root_path, 'seed.csv'), 'w')
for item in random_seed:
    seed_submit.write("%s\n" % item)


f_submit = open(os.path.join(root_path, 'submit.csv'), 'w')
f_submit.write('image,ALB,BET,DOL,LAG,NoF,OTHER,SHARK,YFT\n')
for i, image_name in enumerate(test_image_list):
    pred = ['%.6f' % p for p in predictions[i, :]]
    print('{} / {}'.format(i, nbr_test_samples))
    f_submit.write('%s,%s\n' % (os.path.basename(image_name), ','.join(pred)))

f_submit.close()
