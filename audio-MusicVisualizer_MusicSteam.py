import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf


def music_visualizer(file_path):
    # Load the audio file
    audio_data, samplerate = sf.read(file_path, dtype='float32')
    blocksize = 256
    buffer = np.zeros((blocksize,), dtype=np.float32)

    def audio_callback(outdata, frames, time, status):
        nonlocal audio_data, buffer
        if audio_data.ndim == 1:
            buffer = audio_data[:frames]
            audio_data = audio_data[frames:]
            outdata[:] = buffer.reshape((frames, 1))
        else:
            buffer = audio_data[:frames, 0]
            audio_data = audio_data[frames:]
            outdata[:] = buffer.reshape((frames, 1))

    # Prepare the matplotlib figure
    plt.ion()
    fig, ax = plt.subplots()
    num_bars = 50
    bar_width = 5.5  # Task 4: Adjust the width of the bars
    spacing = 2.0  # Task 4: Adjust the space between the bars
    freq_indices = np.linspace(0, blocksize // 2, num_bars, endpoint=False, dtype=int)
    bars = ax.bar(np.arange(num_bars) * spacing, np.zeros(num_bars), width=bar_width,
                  color='skyblue')  # Task 1: Change the color of the bars
    ax.set_ylim(0, 1)

    # Task 2: Add a grid to the visualization
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

    # Task 3: Add labels to the axes
    ax.set_xlabel('Frequency Bin Index')
    ax.set_ylabel('Magnitude')

    # Task 5: Modify the window function
    window = np.blackman(blocksize)  # Use the Blackman window instead of Hanning

    # Task 6: Adjust the blocksize and FFT size
    fft_size = 2048
    window = np.pad(window, (0, fft_size - blocksize), mode='constant')

    # Start the audio stream
    stream = sd.OutputStream(samplerate=samplerate, channels=1, blocksize=blocksize, callback=audio_callback)
    with stream:
        while len(audio_data) > 0:
            # Resize the buffer to match the window size and apply the window function
            padded_buffer = np.pad(buffer, (0, fft_size - blocksize), mode='constant')

            # Calculate the FFT and normalize the magnitudes
            fft = np.fft.rfft(padded_buffer * window, n=fft_size)  # Apply the chosen window function and FFT size
            magnitudes = np.abs(fft) / (blocksize // 2)
            magnitudes = magnitudes[freq_indices]

            # Update the bar heights
            for bar, magnitude in zip(bars, magnitudes):
                bar.set_height(magnitude)

            plt.pause(blocksize / samplerate)
            fig.canvas.draw()

    plt.ioff()
    plt.show()

file_path = "StarWars60.wav"
music_visualizer(file_path)
