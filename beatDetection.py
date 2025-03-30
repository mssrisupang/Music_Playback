import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from aubio import source, tempo


def display_waveform_with_beats(file_path):
    audio = AudioSegment.from_file(file_path)

    # Convert audio data to numpy array
    audio_data = np.array(audio.get_array_of_samples())
    audio_data = audio_data / (2 ** 15)

    # Set up beat detection
    win_s = 512
    hop_s = win_s // 2
    samplerate = audio.frame_rate
    s = source(file_path, samplerate, hop_s)
    o = tempo("default", win_s, hop_s, samplerate)

    # Collect beat positions
    beats = []
    while True:
        samples, read = s()
        is_beat = o(samples)
        if is_beat:
            beats.append(o.get_last_s())
        if read < hop_s:
            break

    # Plot the audio data
    plt.figure(figsize=(12, 4))
    plt.plot(audio_data)

    # Plot the detected beats
    for beat in beats:
        plt.axvline(x=beat * samplerate, color='r', linestyle='-')

    plt.title('Audio Waveform with Detected Beats')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.show()


# Replace "your_audio_file.mp3" with the path to your audio file
file_path = "StarWars60.wav"
display_waveform_with_beats(file_path)
