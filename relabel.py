import csv
import sys
import os

with open('relabel.txt', 'rb') as f:
    relabel = csv.reader(f)
    for row in relabel:
        old_img_path = row[0].split('_r')[0].split('/')[0]+'_fish/'+row[0].split('_r')[0].split('/')[1]
        new_img_path = row[1]+'_fish/'
        os.system('cp %s_* %s' % (old_img_path,new_img_path))


with open('relabel.txt', 'rb') as f:
    relabel = csv.reader(f)
    for row in relabel:
        old_img_path = row[0].split('_r')[0].split('/')[0]+'_fish/'+row[0].split('_r')[0].split('/')[1]
        os.system('rm %s_*' % (old_img_path))


os.system('mv ALB_fish/img_01452_box0.jpg LAG_fish/')
