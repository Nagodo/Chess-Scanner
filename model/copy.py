from fileinput import filename
import os
import random
import shutil

splitSize = .85

# show the list of folders
dataDirList = os.listdir("./model/Chess")
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

BishopSourceDir = "./model/Chess/Bishop/" #dont forget the last "/"
BishopTrainDir = "./model/train/Bishop/" #dont forget the last "/"
BishopValDir = "./model/validation/Bishop/" #dont forget the last "/"

KingSourceDir = "./model/Chess/King/" #dont forget the last "/"
KingTrainDir = "./model/train/King/" #dont forget the last "/"
KingValDir = "./model/validation/King/" #dont forget the last "/"

KnightSourceDir = "./model/Chess/Knight/" #dont forget the last "/"
KnightTrainDir = "./model/train/Knight/" #dont forget the last "/"
KnightValDir = "./model/validation/Knight/" #dont forget the last "/"

PawnSourceDir = "./model/Chess/Pawn/" #dont forget the last "/"
PawnTrainDir = "./model/train/Pawn/" #dont forget the last "/"
PawnValDir = "./model/validation/Pawn/" #dont forget the last "/"

QueenSourceDir = "./model/Chess/Queen/" #dont forget the last "/"
QueenTrainDir = "./model/train/Queen/" #dont forget the last "/"
QueenValDir = "./model/validation/Queen/" #dont forget the last "/"

RookSourceDir = "./model/Chess/Rook/" #dont forget the last "/"
RookTrainDir = "./model/train/Rook/" #dont forget the last "/"
RookValDir = "./model/validation/Rook/" #dont forget the last "/"

split_data(BishopSourceDir,BishopTrainDir,BishopValDir,splitSize)
split_data(KingSourceDir,KingTrainDir,KingValDir,splitSize)
split_data(KnightSourceDir,KnightTrainDir,KnightValDir,splitSize)
split_data(PawnSourceDir,PawnTrainDir,PawnValDir,splitSize)
split_data(QueenSourceDir,QueenTrainDir,QueenValDir,splitSize)
split_data(RookSourceDir,RookTrainDir,RookValDir,splitSize)