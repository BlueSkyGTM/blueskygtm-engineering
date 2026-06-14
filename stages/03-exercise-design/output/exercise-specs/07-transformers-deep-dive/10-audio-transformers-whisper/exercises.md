# Exercises — Audio Transformers â€” Whisper Architecture

## Exercises

1. **Implement a basic Whisper transcription pipeline.** Load the `base` Whisper model and transcribe the audio file at `data/calls/sample_call.wav`. Print the detected language code, the full transcript, and each segment's text with its start and end timestamps to the terminal. Confirm your output shows a detected language, readable transcript text, and timestamps that span the file's duration.

2. **Trace the encoder-decoder pipeline at each stage.** Using the `tiny` model, capture and print the tensor shape at three points: the log-Mel spectrogram before it enters the encoder, the encoder output after the convolutional stem and self-attention layers, and the first decoder forward-pass logits. Label each stage in your terminal output so the data flow reads end-to-end from spectrogram to token logits.

3. **Compare Whisper output on speech versus silence.** Generate a 10-second silent WAV file using `ffmpeg` (or Python's `wave` module) and transcribe it alongside `data/calls/sample_call.wav` using the same model. Print both transcripts. Document the hallucination pattern: what text does Whisper fabricate during silence, and how do segment confidences differ between the two clips? Print your findings as a structured summary to the terminal.

4. **Build a batch call-processing pipeline for CRM enrichment.** Place three or more audio files in `data/calls/`. Write a script that transcribes every file in the directory and emits a single JSON array to stdout where each element contains `call_id`, `language`, `duration_seconds`, `full_transcript`, and a `segments` array (each segment having `start`, `end`, `text`). Redirect output to `outputs/call_transcripts.json` and validate it with `python -m json.tool`.

5. **Implement confidence-based segment filtering for GTM workflows.** Extend your pipeline from Exercise 4 to extract per-segment confidence scores. Add a CLI argument for a confidence threshold (default `0.7`) and suppress any segment below it. Emit a markdown report to `outputs/skill-call-transcription.md` containing each call's surviving segments, the count of dropped segments per call, and a recommendation section explaining which threshold you would use for sales-call transcripts and why.

6. **Design an end-to-end call signal handler.** Build a Python module at `handlers/call_processor.py` that ingests a directory of recordings, transcribes them with Whisper, filters low-confidence segments, detects language, extracts candidate action items via keyword matching (e.g., "follow up," "send," "schedule," "next steps"), and outputs structured JSON ready for a CRM enrichment step. Run the handler on `data/calls/` and print the final JSON payload to the terminal. Include a module-level docstring documenting your filtering and extraction strategy.
