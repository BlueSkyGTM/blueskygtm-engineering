# Exercises — Music Generation â€” MusicGen, Stable Audio, Suno, and the Licensing Earthquake

## Exercises

1. **Generate a MusicGen clip and inspect the EnCodec token sequence.** Load the `facebook/musicgen-small` model, generate a 10-second instrumental clip from the prompt `"upbeat funk bassline with brass stabs"`, and access the intermediate EnCodec token tensor before decoding. Print the token tensor shape, dtype, per-codebook min/max token values, and a histogram of token frequencies for the first codebook. Save the decoded audio to `outputs/musicgen_tokens.wav`.

2. **Compare text conditioning by generating two clips with opposing prompts.** Using the same MusicGen model and fixed random seed, generate two 10-second clips: one with `"fast aggressive techno, 140 bpm"` and one with `"slow ambient pads, drone, cinematic"`. Compute and print the spectral centroid, zero-crossing rate, and RMS energy for each clip using `librosa`. State which clip has higher spectral brightness and verify it matches the prompt intent.

3. **Measure temporal coherence degradation across generation durations.** Generate three clips from the same prompt (`"jazzy piano trio with walking bass"`) at 5, 15, and 30 seconds. For each clip, compute a mel-spectrogram and calculate the mean absolute frame-to-frame spectral difference as a coherence proxy. Print a duration-vs-coherence table and identify the duration threshold where coherence begins to degrade.

4. **Implement a rule-based architecture classifier from spectrogram features.** Obtain six audio clips — three generated autoregressively (MusicGen) and three via latent diffusion (Stable Audio Open or comparable). For each clip, compute spectral flatness
