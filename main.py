from ultralytics import YOLO
import os

model = YOLO('yolov8n-cls.pt') # ładowanie przetrenowanego modelu (Rekomendowane do trenowania)

model.train(data = os.getcwd() + '/new_data', epochs=20, imgsz = 416)