from ultralytics import YOLO

if __name__ == '__main__':
    
    model = YOLO("yolov8n.yaml")  # build a new model from YAML
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
    model = YOLO("yolov8n.yaml").load("yolov8n.pt")  # build from YAML and transfer weights

    # Train the model
    results = model.train(data="C:/Users/ADITYA/Desktop/Handwritten Texts/config.yaml", epochs=250, imgsz=640, device=0)
