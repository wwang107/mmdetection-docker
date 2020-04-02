from mmdet.apis import init_detector, inference_detector


class BBextractor:
    """
    The bouding box extractor for human in the image
    """

    def __init__(self, configFile, checkpointFile, device="cuda:0"):
        self.model = init_detector(configFile, checkpointFile, device)

    def getPersonBBox(self, img):
        """
        Inference the bouding box of huamn(s) in a single image
        Params:
        img: path to image or a loaded image
        """
        result = inference_detector(self.model, img)
        return [result[0]], ["Person"]
