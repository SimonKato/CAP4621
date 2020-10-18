import os
import shutil
import sys

#get arguments
args = sys.argv
if len(args) != 3:
    raise Exception("Structure: python decouple.py in")

masked = args[1]
unmasked = args[2]
counter = 0
print(masked)
print(unmasked)

for root, subDir, files in os.walk(masked):
    if files:
        for file in files:
            shutil.copyfile(root + '/' + file, "/content/pytorch-CycleGAN-and-pix2pix/datasets/cap_dataset/masked/" + str(counter) + file)
            counter += 1
    else:
        continue

counter = 0
for root, subDir, files in os.walk(unmasked):
    if files:
        for file in files:
            shutil.copyfile(root + '/' + file, "/content/pytorch-CycleGAN-and-pix2pix/datasets/cap_dataset/unmasked/" + str(counter) + file)
            counter += 1
    else:
        continue
