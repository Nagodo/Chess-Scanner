# Create the CNN model

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Conv2D , MaxPooling2D , Flatten, Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping , ModelCheckpoint
from glob import glob

imgWidth = 256
imgHeight = 256
batchSize = 32
numOfEpochs = 10

TRAINING_DIR = "./model/train"

NumOfClasses = len(glob('./model/train/*')) # dont forget the '  /*  '
print (NumOfClasses) # 6 classes

# data augmentation to increase the train data

train_datagen = ImageDataGenerator(rescale = 1/255.0, #normalize between 0 - 1
                                    rotation_range = 30 ,
                                    zoom_range = 0.4 ,
                                    horizontal_flip=True,
                                    shear_range=0.4)

train_generator = train_datagen.flow_from_directory(TRAINING_DIR,
                                                    target_size=(imgWidth,imgHeight),   
                                                    batch_size=batchSize,
                                                    class_mode='categorical')

# create the validation data generator
validation_DIR = "./model/validation"
val_datagen = ImageDataGenerator(rescale = 1/255.0)

val_generator = val_datagen.flow_from_directory(validation_DIR,
                                                    target_size=(imgWidth,imgHeight),
                                                    batch_size=batchSize,
                                                    class_mode='categorical')

# create the model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(imgWidth,imgHeight,3)),
    MaxPooling2D(2,2),

    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Flatten(),
    Dropout(0.5),
    Dense(512, activation='relu'),
    Dense(NumOfClasses, activation='softmax')
])

model.summary()

# compile the model
model.compile(loss='categorical_crossentropy',
                optimizer=Adam(learning_rate=0.001),
                metrics=['accuracy'])

# create the early stopping callback
early_stopping = EarlyStopping(monitor='val_loss', patience=3)

# create the model checkpoint callback
model_checkpoint = ModelCheckpoint('model.h5', monitor='val_loss', save_best_only=True)

# train the model
history = model.fit(train_generator,
                    epochs=numOfEpochs,
                    validation_data=val_generator,
                    callbacks=[early_stopping, model_checkpoint])

# save the model
model.save('model.h5')


