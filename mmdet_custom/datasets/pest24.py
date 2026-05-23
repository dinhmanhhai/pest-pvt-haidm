from mmdet.datasets import DATASETS
from mmdet.datasets.voc import VOCDataset


@DATASETS.register_module()
class Pest24Dataset(VOCDataset):
    """Pest24 dataset, VOC-format annotations with 24 non-sequential
    numeric class labels.
    """

    CLASSES = ('1', '2', '3', '5', '6', '7', '8', '10', '11', '12', '13', '14',
               '15', '16', '24', '25', '28', '29', '31', '32', '34', '35', '36',
               '37')

    def __init__(self, **kwargs):
        # Bypass VOCDataset.__init__'s VOC2007/VOC2012 path check
        # by calling the grandparent (XMLDataset) initializer directly.
        super(VOCDataset, self).__init__(**kwargs)
        # mmdet's VOC mAP evaluator branches on self.year for IoU thresholds;
        # use 2007 semantics (single IoU = 0.5) which is what the paper uses.
        self.year = 2007