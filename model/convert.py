from ultralytics import YOLO

model = YOLO("licensebest.pt")
model.export(format="onnx")
