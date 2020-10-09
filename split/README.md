# `REU Split Folder`
Split folders with files (e.g. images) into **train**, **validation** and **test** (dataset) folders.

The input folder should have the following format:

```
input/
    class1/
        00010101_1.mat
        00010101_2.mat
        ...
    class2/
        00010101_1.mat
        ...
    ...
```
This is the format generated when using the deidentify_dataset.m script

Running this script will yield the following:

```
output/
    class1/
        train/
            00010101_1.mat
            ...
        test/
            00010201_1.mat
            ...
        val/
            00010301_1.mat
    class2/
        train/
            00010101_1.mat
            ...
        test/
            00010201_1.mat
            ...
        val/
            00010301_1.mat
```
### CLI

```
Usage:
    python cli.py [--output] [--ratio] [--seed] [--input]
Options:
    --output        path to the output folder. defaults to `output`. Get created if non-existent.
    --ratio         the ratio to split. e.g. for train/val/test `.8 .1 .1` or for train/val `.8 .2`.
    --seed          set seed value for shuffling the items by default a new seed is generated using rand
Example:
    python cli.py --ratio .8 .1 .1 --input "folder_with_images" --output "output_folder"
```

