import os
import re
import glob
from mmdet.apis import init_detector, inference_detector, show_result


class BBoxPipeline:
    def __init__(self, rootFolder):
        super().__init__()
        self.model = None
        self.rootFolder = ""
        self.subjects = []
        self.images = {}
        if os.path.isdir(rootFolder):
            self.rootFolder = rootFolder
            subjects = list(
                filter(lambda x: re.match(r"S[\d]+", x), os.listdir(rootFolder))
            )
            if len(subjects) == 0:
                print("there are no subjects in the folder\n")
            else:
                print(
                    "the folder contains the following subjects:\n",
                    subjects,
                    "\n Construct full path to image",
                )
                for subject in subjects:
                    print("construct path to ", subject)
                    self.images[subject] = {}
                    subjectPath = os.path.join(self.rootFolder, subject)
                    actions = os.listdir(subjectPath)
                    for action in actions:
                        self.images[subject][action] = {}
                        actionPath = os.path.join(subjectPath, action, "imageSequence")
                        cameras = os.listdir(actionPath)
                        for camera in cameras:
                            cameraPath = os.path.join(actionPath, camera)
                            self.images[subject][action][camera] = glob.glob(
                                os.path.join(cameraPath, "*.jpg")
                            )
                    print("subject ", subject, " done!")
                print("path to images complete")
        else:
            print("the provided path does not exist")

    def initDectector(self, config, checkpoint=None, device="cuda:0"):
        """
        directly borrow code from mmdetction
        """
        self.model = init_detector(config, checkpoint, device='cuda:0')

    def getImgPath(self, subject, action, camera):
        return self.images[subject][action][camera]

    def _infer(self, img):
        """
        directly borrow code from mmdetection       
        """
        result = inference_detector(self.model, img)
        # filter out non-person class and label
        return [result[0]] , ["person"]

    def _showResult(self, img, result, classNames, outFile = None):
        return show_result(
                img,
                result,
                classNames,
                score_thr=0.3,
                wait_time=0,
                show=True,
                out_file=outFile)
