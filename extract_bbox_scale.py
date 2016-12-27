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

labels = ['alb','bet','dol','lag','shark','other','yft']

all_json=[]

for label in labels:
	with open('%s.json' %(label)) as data_file:
		data = json.load(data_file)
		all_json.append(data)

all_json = list(itertools.chain(*all_json))
for i,entry in enumerate(all_json):
	image_path = all_json[i]['image_path']
	species = all_json[i]['image_path'].split('/')[1]
	img = cv2.imread(image_path,1)
	for j in range(0,len(all_json[i]['rects'])):
		y1 = int(round(all_json[i]['rects'][j]['y1']))
		y2 = int(round(all_json[i]['rects'][j]['y2']))
		x1 = int(round(all_json[i]['rects'][j]['x1']))
		x2 = int(round(all_json[i]['rects'][j]['x2']))
		sub_img = img[y1:y2,x1:x2]
		height, width, channels = sub_img.shape
		if height < 30 and width < 30:
			next
			# removing errors when manually annotating thousands of fish...
		im_file = all_json[i]['image_path'].split('/')[2].split('_r')[0]
		image_resized = misc.imresize(sub_img, (299,299))
		scipy.misc.toimage(image_resized).save('train/%s_fish/%s_box%s.jpg' %(species,im_file,str(j)))

