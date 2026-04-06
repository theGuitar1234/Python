import numpy as np
import matplotlib.pyplot as plt

# Create a sample time-domain signal
time = np.linspace(0, 1, 500)      # Time vector
freq = 5                           # Frequency of the signal (in Hz)
signal = np.sin(2 * np.pi * freq * time)  # Sine wave with frequency 5 Hz

# Perform FFT
fft_result = np.fft.fft(signal)

# Get the frequency axis
freqs = np.fft.fftfreq(len(signal), d=time[1] - time[0])

# Plotting the original signal and its FFT
plt.figure(figsize=(12, 5))

# Time-domain signal
plt.subplot(1, 2, 1)
plt.plot(time, signal)
plt.title("Time Domain Signal (5 Hz Sine Wave)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Frequency domain (FFT result)
plt.subplot(1, 2, 2)
plt.stem(freqs[:len(signal) // 2], np.abs(fft_result)[:len(signal) // 2])  # Plot only positive frequencies
plt.title("Frequency Domain (FFT)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.show()
