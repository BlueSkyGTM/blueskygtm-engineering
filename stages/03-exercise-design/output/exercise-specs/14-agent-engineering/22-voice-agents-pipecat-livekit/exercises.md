# Exercises — Voice Agents: Pipecat and LiveKit

## Exercises

1. **Implement a minimal Pipecat pipeline** that chains all five stages — Transport → VAD → STT → LLM → TTS → Transport — and run it against the sample audio file included in the lesson (`data/sample-utterance.wav`). Each processor should print its name and the frame type it receives (e.g., `VAD received AudioRawFrame`). Verify that the terminal shows frames flowing through every stage in order before any TTS audio is produced.

2. **Add directional tracing** to the pipeline from Exercise 1. Inside each processor's `process_frame` method, print either `[DOWNSTREAM] <stage_name> → <frame_type>` or `[UPSTREAM] <stage_name> → <frame_type>` depending on the frame's direction. Run the pipeline and confirm the terminal shows at least one UPSTREAM frame (the `UserStartedSpeakingFrame` from VAD) alongside the DOWNSTREAM sequence. Capture the full terminal output as your verification.

3. **Compute per-stage latency** for a complete pipeline run. Attach a timestamp to each frame as it enters a processor, then calculate and print the delta (in milliseconds) for each stage: STT latency, LLM time-to-first-token, and TTS time-to-first-audio. Sum them into a total downstream latency. Run the pipeline and compare your printed total against the 600 ms production budget. Print a `PASS` or `FAIL` verdict.

4. **Implement interruption handling** for a sales-demo voice agent. Wire a `UserStartedSpeakingFrame` handler so that when VAD fires mid-TTS-playback, the pipeline cancels in-flight TTS synthesis and flushes the LLM token queue. Feed the pipeline a test audio stream where the user barges in during the agent's third sentence. The terminal must print `INTERRUPT detected — cancelling TTS at token N` and the agent's output audio must cut off at that point. No scaffold provided — build the handler from scratch.

5. **Build a cold-call qualification voice agent** that uses Apollo or Clay enrichment data as context. The pipeline connects to a CRM prospect record (name, company, title), the LLM generates a personalized opener, and STT captures the prospect's response to a qualifying question. Log the transcript and the qualification result (qualified / disqualified / follow-up) to the terminal. The full implementation should land at `handlers/cold_call_pipeline.py` and be runnable with `python handlers/cold_call_pipeline.py --proset=<id>`.

6. **Write a proof-of-concept and design memo** demonstrating why WebRTC is required for real-time voice transport and why HTTP cannot serve that role. Implement two minimal transport adapters — one WebRTC (via LiveKit), one HTTP long-polling — and run the same pipeline over each. Measure round-trip latency for both, print the comparison table to the terminal, and write the design memo to `outputs/skill-voice-transport-design.md` including the latency numbers, the bidirectional streaming requirement, and the connection-state semantics that make HTTP unsuitable.
