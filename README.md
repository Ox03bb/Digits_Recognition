# Digits Recognition

![Tensorflow](https://img.shields.io/badge/-Tensorflow-ff6f00?style=flat&logo=tensorflow&logoColor=white) ![Keras](https://img.shields.io/badge/-Keras-d00000?style=flat&logo=keras&logoColor=white) ![sklearn](https://img.shields.io/badge/-sklearn-F89C3F?style=flat&logo=scikit%20learn&logoColor=white&labelColor=3294C7) ![FastApi](https://img.shields.io/badge/-FastApi-029385?style=flat&logo=fastapi&logoColor=white)

## Overview
This project is an implementation of a digits recognition system using the XGBoost algorithm. The system achieves a recognition accuracy of 95%. An API for this project is being developed using FastAPI.The project is currently under development 

## Features
- Handwritten digit recognition using XGBoost
- API for model serving (in development)
- Achieves 95% accuracy on the test dataset

## Installation
To get a local copy up and running, follow these steps:

1. Clone the repository
    ```sh
    git clone https://github.com/your-username/digits-recognition.git
    ```
2. Navigate to the project directory
    ```sh
    cd digits-recognition
    ```
3. Install the required dependencies
    ```sh
    pip install -r requirements.txt
    ```

## Usage
To train the model and run the API, follow these steps:

- **Run the FastAPI server**
    ```sh
    py api.py
    ```
    use the folowing endpoint to get the prediction
## API Endpoints
The FastAPI server exposes the following endpoints:

> the api is still under development

## Model Performance
The XGBoost model achieves an accuracy of 95% on the test dataset. Further improvements and fine-tuning are planned.

