from pathlib import Path
import shutil
from ultralytics import YOLO


def main():
    model = YOLO("yolo26l-cls.pt")  
    results = model.train(
        data="fullData",
        epochs=35,  
        imgsz=320,
        batch=16,          
        workers=2,         
        device=0,
        amp=True,          
        cache=False,       
        project="runs/classify",
        name="yolo26l_cls_320",
        exist_ok=True,
    )
    
    best_weights = Path(results.save_dir) / "weights" / "best.pt"

    
    output_dir = Path("saved_models")
    output_dir.mkdir(parents=True, exist_ok=True)
    final_model_path = output_dir / "yolo26l-cls-best.pt"
    shutil.copy2(best_weights, final_model_path)
    print(f"Saved best model weights to: {final_model_path}")

    
    best_model = YOLO(best_weights)  
    best_model.export(format="onnx", imgsz=320)  


if __name__ == "__main__":
    main()
