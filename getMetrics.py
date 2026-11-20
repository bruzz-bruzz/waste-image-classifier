from ultralytics import YOLO

model = YOLO("saved_models/yolo26l-cls-best.pt")  # or "path/to/yolo26l-cls-best.onnx"

metrics = model.val(
    data="data/val",  # Folder containing train/ and val/
    imgsz=320,
    batch=64,
    device=0,  # Use "cpu" if running on CPU
    plots=True,
)

print(f"Top-1 Accuracy: {metrics.top1:.4f}")
print(f"Top-5 Accuracy: {metrics.top5:.4f}")
print("Metrics dict:", metrics.results_dict)
print("Speed (ms/img):", metrics.speed)