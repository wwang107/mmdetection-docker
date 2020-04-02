from poseEstPipeline.BBoxPipeline import BBoxPipeline
from os import path

CONFIG_FILE = "../configs/faster_rcnn_r50_fpn_1x.py"
CHECKPOINT_FILE = "../checkpoints/faster_rcnn_r50_fpn_1x_20181010-3d1b3351.pth"
EXPORT_FOLDER = "/mmdetection/export"

if __name__ == "__main__":
    pipeline = BBoxPipeline("../human36m")
    pipeline.initDectector(CONFIG_FILE, CHECKPOINT_FILE, device="cuda:0")
    imgPath = pipeline.getImgPath("S1", "Directions-1", "54138969")
    for img in imgPath:
        base = path.basename(img)
        bbox, label = pipeline._infer(img)
        pipeline._showResult(img, bbox, label, path.join(EXPORT_FOLDER, base))
        