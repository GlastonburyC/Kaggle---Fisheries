# ssh craig@86.7.126.76 -N -L 6006:127.0.0.1:6006 
# tensorboard training in realtime: 127.0.0.1:6006
import json
import itertools
import random
from scipy.misc import imread
import cv2
import matplotlib.pyplot as plt
import scipy.misc
from scipy import ndimage, misc


with open('30000_val_lstm_rezoom.json') as data_file:
	all_json = json.load(data_file)

for i,entry in enumerate(all_json):
	image_path = '../test_stg1/rescaled/'+all_json[i]['image_path']
	#species = all_json[i]['image_path'].split('/')[1]
	img = cv2.imread(image_path,1)
	for j in range(0,len(all_json[i]['rects'])):
		score = all_json[i]['rects'][j]['score']
		y1 = int(round(all_json[i]['rects'][j]['y1']))
		if y1 < 0:
			y1 = 0
		y2 = int(round(all_json[i]['rects'][j]['y2']))
		if y2 < 0:
			y2 = 0
		x1 = int(round(all_json[i]['rects'][j]['x1']))
		if x1 < 0:
			x1 = 0
		x2 = int(round(all_json[i]['rects'][j]['x2']))
		if x2 < 0:
			x2 = 0
		if score > 0.5:
			sub_img = img[y1:y2,x1:x2]
			height, width, channels = sub_img.shape
			if height < 30 and width < 30:
				next
				# removing errors when manually annotating thousands of fish...
			else:
				im_file = all_json[i]['image_path'].split('.')[0]
				image_resized = misc.imresize(sub_img, (299,299))
				scipy.misc.toimage(image_resized).save('../test_stg1/test_fishes/%s_box%s.jpg' %(im_file,str(j)))

