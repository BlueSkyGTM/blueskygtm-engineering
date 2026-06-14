# Exercises — Voice Anti-Spoofing & Audio Watermarking â€” ASVspoof 5, AudioSeal, WaveVerify

## Exercises

1. Run the lesson's countermeasure model on the two sample clips (`bonafide.wav` and `spoof_tts.wav`). Print the CM score for each alongside the decision threshold and the resulting verdict. Then shift the threshold by +0.05 and −0.05 and re-classify — report which clips (if any) flip verdict, and explain in one terminal line why the threshold shift matters operationally.

2. Use AudioSeal's encoder to watermark the synthetic TTS clip from the lesson assets. Save the watermarked waveform as a WAV file, reload it from disk, and run the detector. Print detection confidence before saving, after reloading, and a single boolean confirming watermark persistence on disk.

3. Simulate codec degradation: encode the watermarked clip as MP3 at 128 kbps, 64 kbps, and 32 kbps, decode each back to PCM at the original sample rate, and run the detector. Print a terminal table of `bitrate → watermark_confidence`. Report the lowest bitrate at which the watermark survives above a
