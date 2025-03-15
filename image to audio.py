# import numpy as np
# from PIL import Image
# import librosa
# import soundfile as sf
# import wave

# def spectrogram_image_to_audio(img_path, output_audio_path, sr=30203):
#     # Load the spectrogram image
#     img = Image.open(img_path)
#     img = np.array(img)

#     # Normalize the image data back to the range [0, 1]
#     img = img.astype(np.uint8) / 255.0
    
#     # Assuming log_S is known or recalculated based on original settings
#     log_S_min = -80  # Example value, should be adjusted based on the original process
#     log_S_max = 0    # Example value, should be adjusted based on the original process

#     # Convert from dB scale back to amplitude
#     log_S = img * (log_S_max - log_S_min) + log_S_min
#     S = librosa.db_to_amplitude(log_S)
    
#     # Reconstruct the original audio signal from the Mel spectrogram
#     y = librosa.feature.inverse.mel_to_audio(S, sr=sr, n_fft=2048, hop_length=512)
    
#     # Save the reconstructed audio signal to a file
#     sf.write(output_audio_path, y, sr)

# # Example usage
# img_path = 'specto/ringtone-205162.png'
# output_audio_path = 'reconstructed_audio.wav'
# spectrogram_image_to_audio(img_path, output_audio_path)

import librosa
import pickle
import numpy as np
import soundfile as sf

with open('audio_array.pkl', 'rb') as f:
    audio = pickle.load(f)
    audio = np.array(audio)

sf.write('generated_audio.wav', audio, samplerate=22050)
