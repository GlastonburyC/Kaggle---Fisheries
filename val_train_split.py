# ssh craig@86.7.126.76 -N -L 6006:127.0.0.1:6006 
# tensorboard training in realtime: 127.0.0.1:6006
import json
import itertools
import random

valp = 0.20
trainp = 0.80

labels = ['alb','bet','dol','lag','shark','other','yft']

all_json=[]

for label in labels:
	with open('%s.json' %(label)) as data_file:
		data = json.load(data_file)
		all_json.append(data)

all_json = list(itertools.chain(*all_json))

random.shuffle(all_json)

prop = int(round(len(all_json)*valp))

train_data = all_json[prop:]
test_data = all_json[:prop]

with open('train80.json', 'w') as json_file:
	json.dump(train_data,json_file, ensure_ascii=False,indent=4)

with open('validation20.json', 'w') as json_file:
	json.dump(test_data,json_file, ensure_ascii=False,indent=4)
