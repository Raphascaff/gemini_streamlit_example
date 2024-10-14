# Voice Prompt Generator with Streamlit

## Overview

This project is a **Voice Prompt Generator** built using Streamlit, which allows users to record voice messages and generate content using the Google Generative AI model. Users can input text prompts and upload audio recordings to create responses based on their inputs.

## Features

- **Text Input**: Enter prompts using a text area.
- **Audio Recording**: Record voice messages using an audio input feature.
- **Content Generation**: Generate content using the Google Generative AI model based on the text and audio inputs.
- **Clear Functionality**: Clear all input fields with a single button.

## Prerequisites

- Python 3.7 or higher
- Streamlit
- Google Generative AI client library
- dotenv for environment variable management

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/voice-prompt-generator.git
   cd voice-prompt-generator

### Creating Virtual Enviroment
```bash
python -m venv venv
```

Accessing -> venv\Scripts\activate For windows or source venv/bin/activate mac/linux

### Get your own Gemini key
gemini_api_key=your_google_generative_ai_api_key

### Install Requirements
```bash
pip install -r requirements.txt
```
### Run
```bash
streamlit run main.py
```

