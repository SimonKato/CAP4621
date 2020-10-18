import os
import shutil

for root, subDir, files in os.walk("/home/kato/docs/UF/s5/ai/project/pytorch-CycleGAN-and-pix2pix/datasets/self-built-masked-face-recognition-dataset/AFDB_face_dataset"):
    if files:
        for file in files:
            shutil.copyfile(root + '/' + file, "/home/kato/docs/UF/s5/ai/project/pytorch-CycleGAN-and-pix2pix/datasets/cap_dataset/unmasked/" + file)
    else:
        continue

for root, subDir, files in os.walk("/home/kato/docs/UF/s5/ai/project/pytorch-CycleGAN-and-pix2pix/datasets/self-built-masked-face-recognition-dataset/AFDB_masked_face_dataset"):
    if files:
        for file in files:
            shutil.copyfile(root + '/' + file, "/home/kato/docs/UF/s5/ai/project/pytorch-CycleGAN-and-pix2pix/datasets/cap_dataset/masked/" + file)
    else:
        continue