import os
import shutil

counter = 0

for root, subDir, files in os.walk("/content/pytorch-CycleGAN-and-pix2pix/datasets/cloned-repo-masked"):
    if files:
        for file in files:
            shutil.copyfile(root + '/' + file, "/content/pytorch-CycleGAN-and-pix2pix/datasets/cap_dataset/masked/" + str(counter) + file)
            counter += 1
    else:
        continue

counter = 0
for root, subDir, files in os.walk("/content/pytorch-CycleGAN-and-pix2pix/datasets/cloned-repo-unmasked"):
    if files:
        for file in files:
            shutil.copyfile(root + '/' + file, "/content/pytorch-CycleGAN-and-pix2pix/datasets/cap_dataset/unmasked/" + str(counter) + file)
            counter += 1
    else:
        continue
