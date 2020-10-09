import os
import pathlib
import random
from sklearn.model_selection import train_test_split

"""
Main Concerns/Possible Changes
    Parsing the fileName from the windowspath file, uses rfind and then because
    window pathing is \\ instead of / parses the fileName as [rfind + 2:]

    In the hopes of increasing effiency I pop patients as to have that the file
    which is being considered is alwys the head of one of the split lists. In order
    to do this I delete entries of the list after moving on to a higher number.
    Since python passes by reference, this would destroy the splits which we need
    to avoid data leakage.
        Current resolution: create dummy copies of the splits each time a different
        modality is divided up.
        Possible solution: populate a set with the numbers of the list and have
        quick access time.
"""

def split_patients(startIndex, endIndex, seed, ratio):
    numPatients = range(startIndex, endIndex + 1)

    if float(ratio[1]) == 0:
        test_train = train_test_split(numPatients, test_size=ratio[2],
                                     random_state=seed, shuffle=True)

        trainSplit = test_train[0]
        valSplit = []
        testSplit = test_train[1]

        trainSplit.sort()
        testSplit.sort()
    else:
        tempSplit = train_test_split(numPatients, test_size = ratio[2], random_state = seed, shuffle = True)

        train_val = tempSplit[0]
        testSplit = tempSplit[1]

        trainvalSplit = train_test_split(train_val, test_size = ratio[1], random_state= seed, shuffle = True)

        trainSplit = trainvalSplit[0]
        valSplit = trainvalSplit[1]

        trainSplit.sort()
        valSplit.sort()
        testSplit.sort()

    return trainSplit, valSplit, testSplit

def splitModality(modalityPath, outputPath, trainSplit, valSplit, testSplit):
    #Couple ideas: make the splits into sets for quick look up if the list_files are not in order of increasing numbers
    os.mkdir(os.path.join(outputPath, 'test'))
    os.mkdir(os.path.join(outputPath, 'train'))
    if valSplit != []:
        os.mkdir(os.path.join(outputPath, 'val'))

    modality_files = list_files(modalityPath)
    lastPatient = 0;

    for file in modality_files:
        fileName = (str(file))[str(file).rfind('\\') + 1:] #might be issue since it assumes windows path?
        curPatient = int(fileName[:6])

        if curPatient != lastPatient:
            pop_patient(trainSplit, valSplit, testSplit, curPatient)
            lastPatient = curPatient

        if len(trainSplit) > 0 and curPatient == trainSplit[0]:
            os.rename(file, os.path.join(outputPath, 'train', fileName))
        elif len(valSplit) > 0 and curPatient == valSplit[0]:
            os.rename(file, os.path.join(outputPath, 'val', fileName))
        elif len(testSplit) > 0 and curPatient == testSplit[0]:
            os.rename(file, os.path.join(outputPath, 'test', fileName))
        else:
            #This is where we would have an issue since we're calling pop_patient before checking.
            pass
    return

def list_files(directory):
    """Returns all files in a given directory function from split-folders by jfilter
    """
    return [
        f
        for f in pathlib.Path(directory).iterdir()
        if f.is_file() and not f.name.startswith(".")
    ]

def list_dirs(directory):
    """Returns all directories in a given directory written by split-folders jfilter
    """
    return [f for f in pathlib.Path(directory).iterdir() if f.is_dir()]

def pop_patient(trainSplit, valSplit, testSplit, curPatient):
    while len(trainSplit) > 0 and trainSplit[0] < curPatient:
        trainSplit.remove(trainSplit[0])

    while len(valSplit) > 0 and valSplit[0] < curPatient:
        valSplit.remove(valSplit[0])

    while len(testSplit) > 0 and testSplit[0] < curPatient:
        testSplit.remove(testSplit[0])

def split_dataset(inputPath, outputPath,  ratio = (0.8, 0.1, 0.1), seed = random.seed()):
    if not os.path.isdir(outputPath):
        os.mkdir(outputPath)

    startIndex, endIndex = get_range(inputPath)
    trainSplit, valSplit, testSplit = split_patients(startIndex, endIndex, seed, ratio)

    for fullDir in list_dirs(inputPath):
        fullDir = str(fullDir)
        modality = fullDir[fullDir.rfind('\\') + 1:]
        #These Copies are created for the sake of increasing run time efficiency, it very well might not be worth the space it takes up
        #I do not know when it would become worth it to create these copies.
        tempTrainSplit = trainSplit.copy()
        tempValSplit = valSplit.copy()
        tempTestSplit = testSplit.copy()

        if not os.path.isdir(os.path.join(outputPath, modality)):
            os.mkdir(os.path.join(outputPath, modality))

        splitModality(os.path.join(inputPath, modality), os.path.join(outputPath, modality), tempTrainSplit, tempValSplit, tempTestSplit)

def get_range(inputPath):
    dirs = list_dirs(inputPath)
    files = list_files(os.path.join(inputPath, dirs[0]))
    first_file = files[0]
    last_file = files[len(files)-1]

    first_filename = (str(first_file))[str(first_file).rfind('\\') + 1:]  # might be issue since it assumes windows path?
    startIndex = int(first_filename[:6])

    last_filename = (str(last_file))[str(last_file).rfind('\\') + 1:]  # might be issue since it assumes windows path?
    endIndex = int(last_filename[:6])

    return startIndex, endIndex
