# AI-The-Past-and-the-Present

A Python application that demonstrates the evolution of AI by comparing ELIZA, a classic rule-based chatbot from the 1960s, with a modern Large Language Model (LLM) using the Qwen2.5-1.5B-Instruct model.

## Features

- **Side-by-Side Comparison**: Interactive GUI showing responses from both ELIZA and LLM simultaneously.
- **ELIZA Implementation**: Rule-based conversational AI using NLTK's ELIZA chatbot.
- **LLM Integration**: Modern generative AI powered by Hugging Face Transformers.
- **User-Friendly Interface**: Built with Tkinter for easy interaction.

## Requirements

- Python 3.7+
- Required packages:
  - `nltk`
  - `transformers`
  - `torch` (for model inference)
  - `tkinter` (usually included with Python)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Elbowg/AI-The-Past-and-the-Present.git
   cd AI-The-Past-and-the-Present
   ```

2. Install dependencies:
   ```
   pip install nltk transformers torch
   ```

3. Download NLTK data (for ELIZA):
   ```
   python -c "import nltk; nltk.download('punkt')"
   ```

## Usage

Run the main application:
```
python chat_comparison.py
```

This launches a GUI window where you can type messages and see responses from both AI systems.

You can also run individual components:
- ELIZA only: `python eliza.py`
- LLM only: `python LLM.py`

## Files

- `chat_comparison.py`: Main GUI application for comparing ELIZA and LLM.
- `eliza.py`: ELIZA chatbot implementation.
- `LLM.py`: LLM chatbot using Qwen model.

## License

This project is open-source. Please refer to the repository for licensing details.