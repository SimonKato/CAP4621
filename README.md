# CAP4621
CAP4621 Project

## Dependencies 
Refer to https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix for depencies for the CycleGAN.
Futhermore, https://github.com/jfilter/split-folders has a pip install which must be ran in order to preprocess the data.
decouple.py must also be run after split-folders has been run.

# Notes about files
 - CycleGAN code in CAP4621.ipynb
 - Discriminator code in CAP4621_Discriminator.ipynb
 - decouple.py includes image preprocessing and face recognition
 - deploy.prototype.txt, haarcascade_frontalface_default.xml, and res10_300x300_ssd_iter_140000.caffemodel are all prebuilt models from opencv

# Important Note:
be sure to use the --continue_train parameter to continue training. The epoch which was last used was --epoch_count 2

# Asssumed Input Data Structure:
```
  ├── Data (Dataset Folder)  
     └── Masked 
       └── Person_1  
           ├── image_1.jpg
           ├── image_2.jpg
           ├── image_3.jpg
           ├── ...
       └── Person_2
           ├── image_1.jpg
           ├── image_2.jpg
           ├── image_3.jpg
           ├── ...
       └── Person_3
           ├── image_1.jpg
           ├── image_2.jpg
           ├── image_3.jpg
           ├── ...
       └──...  
         
     └── Unmasked 
       └── Person_1  
           ├── image_1.jpg
           ├── image_2.jpg
           ├── image_3.jpg
           ├── ...
       └── Person_2
           ├── image_1.jpg
           ├── image_2.jpg
           ├── image_3.jpg
           ├── ...
       └── Person_3
           ├── image_1.jpg
           ├── image_2.jpg
           ├── image_3.jpg
           ├── ...
       └──...        
       
```

# CycleGAN Assumed
```
  ├── Data (Dataset Folder)  
     └── TrainA
        ├── image_1.jpg
        ├── image_2.jpg
        ├── image_3.jpg
        ├── ...    
     └── TrainB
        ├── image_1.jpg
        ├── image_2.jpg
        ├── image_3.jpg
        ├── ...
     └──TestA
        ├── image_1.jpg
        ├── image_2.jpg
        ├── image_3.jpg
        ├── ...
     └──TestB
        ├── image_1.jpg
        ├── image_2.jpg
        ├── image_3.jpg
        ├── ...
     └──ValA (optional)
        ├── image_1.jpg
        ├── image_2.jpg
        ├── image_3.jpg
        ├── ...
     └──ValB (optional)
        ├── image_1.jpg
        ├── image_2.jpg
        ├── image_3.jpg
        ├── ...
     
```
