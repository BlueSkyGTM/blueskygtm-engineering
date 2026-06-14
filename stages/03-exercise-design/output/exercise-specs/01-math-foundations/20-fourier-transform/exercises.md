# Exercises — The Fourier Transform

## Exercises

1. **Implement** a composite signal from three sinusoids at 5 Hz, 12 Hz, and 25 Hz with amplitudes 3.0, 1.5, and 0.8 respectively. Sample at 100 Hz for 2 seconds. Apply `np.fft.fft`, compute the magnitude spectrum, and write a loop that prints the top three spectral peaks alongside the known frequencies and amplitudes. Confirm that the recovered peaks match your inputs to within one bin width.

2. **Compute** the frequency bin width (Δf = fs / N) for two sample counts: N = 128 and N = 1024, both at fs = 100 Hz. Build a composite signal containing two closely spaced sinusoids at 10.0 Hz and 10.8 Hz. Run the FFT for both N values and print the magnitude spectrum around the relevant bins. Report which N resolves the two peaks as distinct and which merges them into a single bump. Print the bin indices and frequencies for both cases.

3. **Apply** spectral cycle detection to a mystery
