    # Form-OCR-using-YOLO

    This project demonstrates how to perform Optical Character Recognition (OCR) on forms using the YOLOv8 object detection model. It includes scripts for data generation, model training, and prediction.

    ## Files

    *   **config.yaml**: Configuration file for YOLO, defining paths to training and validation data and class names (sign and handwritten).
    *   **dataset_gen.py**: A script for generating synthetic datasets by applying augmentations such as flipping, brightness adjustment, opacity adjustment, rotation, and shearing to existing images. This helps to increase the diversity of the training data.
    *   **photograph.py**: A script that simulates taking photographs of forms. It overlays signature images onto document images to create more realistic training samples.
    *   **predict.py**: Script for performing inference (prediction) on new form images using a trained YOLOv8 model. It loads a model and runs it on a specified source of images, saving the detection results.
    *   **README.md**: The current README file providing an overview of the project.
    *   **yolo.py**: Script for training a YOLOv8 model. It loads a pre-trained model and fine-tunes it on the form OCR dataset.
    *   **yolov8n.pt**: A pre-trained YOLOv8 Nano model, used as a starting point for training.

    ## Overview

    The project utilizes YOLOv8, a state-of-the-art object detection model, to identify and locate specific elements within form images, such as signatures and handwritten text. The scripts provided cover the essential steps in developing and deploying such a model:

    1. **Data Generation**: `dataset_gen.py` is used to augment existing images, creating a larger and more varied dataset for training.
    2. **Synthetic Data Creation**: `photograph.py` creates synthetic form images by overlaying signatures, simulating real-world scenarios.
    3. **Model Training**: `yolo.py` trains the YOLOv8 model using the generated and prepared dataset, fine-tuning it for the specific task of form OCR.
    4. **Prediction**: `predict.py` loads the trained model and uses it to make predictions on new, unseen form images.

    ## Usage

    To use this project, you would typically follow these steps:

    1. **Prepare your dataset**: Organize your form images and annotations.
    2. **Configure `config.yaml`**: Update the paths to your training and validation data.
    3. **Run data generation scripts**: Execute `dataset_gen.py` and `photograph.py` to create augmented and synthetic training data.
    4. **Train the model**: Run `yolo.py` to train the YOLOv8 model.
    5. **Run predictions**: Use `predict.py` to perform OCR on new form images.

    This project provides a foundation for building a robust form OCR system using YOLOv8.
