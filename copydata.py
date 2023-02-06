from fileinput import filename
import os
import random
import shutil

splitSize = .85

# show the list of folders
dataDirList = os.listdir("Chessman-image-dataset/Chess")
print(dataDirList)

# lest vuild a function that will split the data between train and validation

def split_data(SOURCE , TRAINING , VALIDATION , SPLIT_SIZE):

    files = []

    for filename in os.listdir(SOURCE):
        file = SOURCE + filename
        print(file)
        if os.path.getsize(file) > 0 :
            files.append(filename)
        else:
            print(filename + " - would ignore this file")

    print(len(files))

    trainLength = int( len(files) * SPLIT_SIZE)
    validLength = int (len(files) - trainLength)
    shuffledSet = random.sample(files , len(files))

    trainSet = shuffledSet[0:trainLength]
    validSet = shuffledSet[trainLength:]

    # copy the train images :
    for filename in trainSet:
        thisfile = SOURCE + filename
        destination = TRAINING + filename
        shutil.copyfile(thisfile, destination)

    # copy the validation images :
    for filename in validSet:
        thisfile = SOURCE + filename
        destination = VALIDATION + filename
        shutil.copyfile(thisfile, destination)

BishopSourceDir = "Chessman-image-dataset/Chess/Bishop/" #dont forget the last "/"
BishopTrainDir = "Chessman-image-dataset/train/Bishop/" #dont forget the last "/"
BishopValDir = "Chessman-image-dataset/validation/Bishop/" #dont forget the last "/"

KingSourceDir = "Chessman-image-dataset/Chess/King/" #dont forget the last "/"
KingTrainDir = "Chessman-image-dataset/train/King/" #dont forget the last "/"
KingValDir = "Chessman-image-dataset/validation/King/" #dont forget the last "/"

KnightSourceDir = "Chessman-image-dataset/Chess/Knight/" #dont forget the last "/"
KnightTrainDir = "Chessman-image-dataset/train/Knight/" #dont forget the last "/"
KnightValDir = "Chessman-image-dataset/validation/Knight/" #dont forget the last "/"

PawnSourceDir = "Chessman-image-dataset/Chess/Pawn/" #dont forget the last "/"
PawnTrainDir = "Chessman-image-dataset/train/Pawn/" #dont forget the last "/"
PawnValDir = "Chessman-image-dataset/validation/Pawn/" #dont forget the last "/"

QueenSourceDir = "Chessman-image-dataset/Chess/Queen/" #dont forget the last "/"
QueenTrainDir = "Chessman-image-dataset/train/Queen/" #dont forget the last "/"
QueenValDir = "Chessman-image-dataset/validation/Queen/" #dont forget the last "/"

RookSourceDir = "Chessman-image-dataset/Chess/Rook/" #dont forget the last "/"
RookTrainDir = "Chessman-image-dataset/train/Rook/" #dont forget the last "/"
RookValDir = "Chessman-image-dataset/validation/Rook/" #dont forget the last "/"

split_data(BishopSourceDir,BishopTrainDir,BishopValDir,splitSize)
split_data(KingSourceDir,KingTrainDir,KingValDir,splitSize)
split_data(KnightSourceDir,KnightTrainDir,KnightValDir,splitSize)
split_data(PawnSourceDir,PawnTrainDir,PawnValDir,splitSize)
split_data(QueenSourceDir,QueenTrainDir,QueenValDir,splitSize)
split_data(RookSourceDir,RookTrainDir,RookValDir,splitSize)