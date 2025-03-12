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
