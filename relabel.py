import csv
import sys
import os

with open('relabel.txt', 'rb') as f:
    relabel = csv.reader(f)
    for row in relabel:
        old_img_path = row[0]
        new_img_path = row[1]+'/'+row[0].split('/')[1]
        os.system('cp %s %s' % (old_img_path,new_img_path))


with open('relabel.txt', 'rb') as f:
    relabel = csv.reader(f)
    for row in relabel:
        old_img_path = row[0]
        os.system('rm %s' % (old_img_path))

