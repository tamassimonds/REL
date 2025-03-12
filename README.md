# REL (Reasoning Enhancement Loop)

REL is a novel framework for generating synthetic worked solutions to enhance the reasoning capabilities of Large Language Models (LLMs). It acts as a variation to the STaR to more thoughtful worked soltions. This repository contains the implementation of the REL pipeline as described in our [paper](https://arxiv.org/abs/2412.04645).

## Overview

REL demonstrates that by constructing a specialized dataset focused on explicit problem-solving workflows ("worked solutions"), we can elicit substantially improved planning capabilities from existing models. The method combines:

1. High-quality human-annotated worked solutions
2. An iterative critic-generator pipeline for synthetic data generation
3. A novel approach to preserving and enhancing authentic problem-solving processes

## Key Features

- **Human-AI Collaborative Data Creation**: Tools and methodology for creating high-quality worked solutions combining human expertise with LLM capabilities
- **REL Pipeline**: Implementation of the Reasoning Enhancement Loop for generating additional synthetic worked solutions
- **Dataset**: ReasonSet, a collection of worked solutions capturing complete problem-solving processes


## Repository Structure

- `dataset/`: Contains the ReasonSet dataset and training data
- `lib/`: Core library implementations
- `samples/`: Example outputs and demonstrations
- `generate_synthetic_data.py`: Implementation of the REL synthetic data generation pipeline
- `main.py`: Main entry point for running the REL system

## Getting Started

### Prerequisites

[List any prerequisites, Python version, required packages, etc.]

### Installation

```bash
git clone https://github.com/tamassimonds/REL.git
cd REL
pip install -r requirements.txt
```

### Usage

1. **Creating Worked Solutions**:
```python
python main.py --mode create_solutions
```

2. **Running the REL Pipeline**:
```python
python generate_synthetic_data.py
```

## Results

Our experiments demonstrate:

- 18.9% improvement on AIME 2024 compared to baseline models
- Superior scaling properties with REL-generated synthetic data
- Emergence of sophisticated reasoning patterns with just 100 training examples

## Citation

If you use this code or our findings in your research, please cite:

```bibtex
@article{simonds2024rel,
  title={REL: Reasoning Enhancement Loop for Generating Synthetic Worked Solutions},
  author={Simonds, Toby},
  journal={arXiv preprint arXiv:2412.04645},
  year={2024}
}
```

# Core dependencies
torch>=2.0.0
transformers>=4.30.0
numpy>=1.24.0
pandas>=2.0.0

# LLM and API interactions
openai>=1.0.0
anthropic>=0.3.0  # For Claude API interactions
tiktoken>=0.5.0   # For token counting

# Data processing and analysis
scipy>=1.10.0
scikit-learn>=1.2.0

# Text processing
nltk>=3.8.0
spacy>=3.6.0

# Progress tracking and logging
tqdm>=4.65.0
wandb>=0.15.0  # For experiment tracking
tensorboard>=2.13.0

# Development tools
pytest>=7.3.0
black>=23.3.0
isort>=5.12.0
flake8>=6.0.0

# Optional: Speech-to-text (as mentioned in paper for data collection)
SpeechRecognition>=3.10.0
pyaudio>=0.2.13  # For audio input
