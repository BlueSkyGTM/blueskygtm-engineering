# Exercises — Audio Fundamentals â€” Waveforms, Sampling, Fourier Transform

## Exercises

1. **Generate** a 440 Hz sine wave at 16 kHz sample rate for 0.5 seconds with amplitude 1.0 and phase 0.0. Print the first 10 sample values. Then compute the expected analytical value for each sample using `A * sin(2πf·n/sr + φ)` and print those alongside. Confirm the two columns match to at least 6 decimal places. Repeat for frequency 880 Hz and verify that zero-crossings occur twice as often by printing sample indices where the signal changes sign in both cases.

2. **Compute** the FFT of a 1-second, 1000 Hz sine wave sampled at 16 kHz. Print the index of the magnitude-spectrum bin with the highest value. Then implement the bin-index-to-Hz mapping (`freq = bin_index * sr / N`) and print the dominant frequency in Hz. Verify it reports 1000 Hz. Change the signal to a two-tone mix (500 Hz + 2000 Hz) and print the top two detected frequencies — confirm both appear.

3. **Demonstrate** aliasing by generating a continuous 3000 Hz sine wave and sampling it at three different rates: 16 kHz (above Nyquist), 8000 Hz (exactly at Nyquist), and 5000 Hz (below Nyquist). For each sampled version, compute the FFT and print the dominant detected frequency. For the aliased case, compute the expected false frequency using `f_alias = |f - k·fs|` for the nearest integer `k` and verify it matches what the FFT reports. Print a summary table showing sample rate, Nyquist limit, detected frequency, and whether aliasing occurred.

4. **Implement** a rolling-window FFT spectrogram from scratch (no `scipy.signal.spectrogram`). Construct a 5-second test signal at 16 kHz where the first 2 seconds contain a 440 Hz tone and the remaining 3 seconds contain an 880 Hz tone. Use a 25 ms window length with a 10 ms hop size. For each window, compute the FFT and extract the dominant frequency. Print a table of window start time, dominant frequency, and detected tone (440 or 880). Confirm the transition occurs near the 2-second mark. Count how many windows misclassify the tone near the transition boundary and print that count.

5. **Build** a spectral-centroid-based voice activity detector for call analytics pipelines. Generate a 10-second synthetic call signal at 16 kHz: 3 seconds of near-silence (low-amplitude noise), 4 seconds of speech-like content (a sum of harmonics at 80–120 Hz fundamental with formant peaks at 500, 1500, and 2500 Hz plus colored noise), then 3 seconds of near-silence.
