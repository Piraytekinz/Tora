# Tora
Tora is an image to video model built using the pix2pix GAN architecture.

The idea is to train a GAN model which translates the image of a particular frame to the next frame continuously,
where the predicted, generated or translated frame becomes the data for predicting the next frame.

audio to image.py - Loads the audio into an array and dumps it into a pickle file.

chekc.py - A file for performing various image processing techniques on the images to enhance performance.

image to audio.py - Meant for collecting the stored audio arrays and transforming them into audio files.

main.py - In main, we're collecting the frames from a specific movie and using it as training data for the model.

test-model.py - Loads and tests the saved generator model.

Unfortunately, I'm not able to upload the models because of their size.

