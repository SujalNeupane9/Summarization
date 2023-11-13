# Summarization

This project is a machine learning pipeline for natural language processing tasks. It contains a set of scripts and modules that allow you to train and evaluate various models on your own data.


## Project Structure

### `pipeline`
This directory contains the code for the main data pipeline.

- `training_pipeline.py`: Code for the training pipeline.
- `inference_pipeline.py`: Code for the inference pipeline.

### `steps`
This directory includes various steps involved in the data pipeline.

- `evaluation.py`: Code for evaluating the model.
- `ingest_data.py`: Code for ingesting data into the pipeline.
  - `preprocess.py`: Data preprocessing code.
  - `model_train.py`: Model training code.

### `utils`
This directory contains utility functions used throughout the project.

- `utils.py`: General utility functions.

### `run_pipeline.py`
This script is the entry point for running the entire data pipeline.

### `Dockerfile`
The Dockerfile for creating a Docker image for this project.

### `requirements.txt`
List of Python packages required for running the project. Install them using:

## License
This project is licensed under the MIT License - see the LICENSE file for details.
