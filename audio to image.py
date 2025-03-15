# import librosa
# import numpy as np
# from PIL import Image


# def audio_to_spectrogram_image(audio_path, output_image_path):
#     # Load the audio file
#     y, sr = librosa.load(audio_path, sr=None)  # Load the audio file at its native sampling rate
#     # Generate a Mel spectrogram
#     S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=64)

#     # Convert to log scale (dB). We'll use the peak power as reference.
#     log_S = librosa.amplitude_to_db(S, ref=np.max)


#     # Normalize the log_S to the range [0, 255]
#     min_val = np.min(log_S)
#     max_val = np.max(log_S)
#     img = 255 * (log_S - min_val) / (max_val - min_val)
#     img = img.astype(np.uint8)
    
#     # Convert the spectrogram to an image
#     img = Image.fromarray(img, mode='L')


#     # Save the image
#     img.save(output_image_path)



# # Example usage
# # audio_path = 'path/to/your/audio/file.wav'
# # output_image_path = 'spectrogram.png'
# # audio_to_spectrogram_image(audio_path, output_image_path)


# # Example usage
# import os
# for aud in os.listdir('audio'):
#     for audio in os.listdir(os.path.join('audio', aud)):
#         audio_path = "C:/Users/anang/OneDrive/Desktop/Tora/audio/" + aud + '/' + audio
#         output_image_path = f'specto/{audio[:-4]}.png'

#         audio_to_spectrogram_image(audio_path, output_image_path)


import librosa
import pickle

def load_audio(file_path, sr=22050):
    audio, _ = librosa.load(file_path, sr=sr)

    with open('audio_array.pkl', 'wb') as f:
        pickle.dump(audio, f)
    return audio

audio = load_audio('audio/car/audi-v8-acceleration-sound-6067.mp3')