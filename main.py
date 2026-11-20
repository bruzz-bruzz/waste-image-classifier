from pathlib import Path
import shutil
from ultralytics import YOLO


def main():
    model = YOLO("yolo26l-cls.pt")  #

    results = model.train(
        data="data/train",
        epochs=35,  # Use a fixed epoch count (30–40) since early stopping won't detect overfitting
        imgsz=320,
        batch=64,
        workers=8,
        device=0,
        project="runs/classify",
        name="yolo26l_cls_320",
        exist_ok=True,
    )

    # Path to automatically saved checkpoints (best.pt and last.pt)
    best_weights = Path(results.save_dir) / "weights" / "best.pt"

    # Copy best weights to a dedicated location
    output_dir = Path("saved_models")
    output_dir.mkdir(parents=True, exist_ok=True)
    final_model_path = output_dir / "yolo26l-cls-best.pt"
    shutil.copy2(best_weights, final_model_path)
    print(f"Saved best model weights to: {final_model_path}")

    # Optional: load the best checkpoint and export for deployment (e.g., ONNX)
    best_model = YOLO(best_weights)  #
    best_model.export(format="onnx", imgsz=320)  #


if __name__ == "__main__":
    main()