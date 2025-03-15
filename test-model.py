#THIS CODE IS MEANT TO TEST THE AI MODEL AFTER TRAINING

import tensorflow as tf
from matplotlib import pyplot as plt
import os

IMG_WIDTH = 256
IMG_HEIGHT = 256

def load_and_preprocess_image(image_file):
    # Load the image from the file path
    image = tf.io.read_file(image_file)
    # Decode the image (e.g., JPEG or PNG)
    image = tf.image.decode_jpeg(image, channels=3)
    # Resize the image to your desired dimensions
    image = tf.image.resize(image, [IMG_WIDTH, IMG_HEIGHT])
    # Normalize pixel values (optional)
    image = (image / 127.5) - 1

    image = tf.reshape(image, (-1, tf.shape(image)[0], tf.shape(image)[1], tf.shape(image)[2]))

    # image = random_crop(image)
    
    # image = tf.image.random_flip_left_right(image)
    return image

model = tf.keras.models.load_model('generator.h5')
n = 0

for i, img in enumerate(os.listdir(os.path.join('frames'))):
    image = load_and_preprocess_image(f'labels/frame1715.jpg')

    n+=1

    def generate_images(model, test_input):
        img = model(test_input, training=True)

        plt.figure(figsize=(15, 15))

        print(img[0])

        # plt.imsave(os.path.join('predicted_frames', f'frame{n}.jpg'), img[0])

        display_list = [test_input[0], img[0]]
        title = ['Input Image', 'Predicted Image']

        for i in range(2):
            plt.subplot(1, 3, i+1)
            plt.title(title[i])
            # Getting the pixel values in the [0, 1] range to plot.
            plt.imshow(display_list[i] * 0.5 + 0.5)
            plt.axis('off')
        plt.show()

    # if i == 100:
    generate_images(model, image)
    break

    

