
# HRAI

**Human Response Analysis & Intelligence**

An AI-powered multimodal system for speaker identification, speech transcription, and emotion analysis using audio, text, and visual data.

## Features

- Speech-to-Text Transcription
- Speaker Diarization
- Acoustic Feature Extraction
- Audio Emotion Recognition
- Text Sentiment Analysis
- Facial Expression Analysis
- Multimodal Emotion Analysis

## Technologies

- Python 3.11
- OpenAI Whisper
- Librosa
- Pyannote.audio
- OpenCV
- Hugging Face Transformers
- Streamlit

## Project Structure

- `audio/` — Audio processing and NLP
- `vision/` — Computer vision
- `fusion/` — Multimodal analysis
- `app/` — User interface
- `tests/` — Unit and integration tests
- `data/` — Local datasets and recordings

## Development Workflow

- `master` — Stable project version
- `feature/audio-processing` — Audio and NLP development
- `feature/computer-vision` — Computer vision development

## Setup

1. Clone the repository.
2. Create a Python 3.11 virtual environment.
3. Install dependencies:

   `python -m pip install -r requirements.txt`

4. Copy `.env.example` to `.env` and configure the required environment variables.
