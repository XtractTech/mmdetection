from .coco import CocoDataset
from .registry import DATASETS


@DATASETS.register_module
class OISubset(CocoDataset):

    CLASSES = (
        'person', 'bicycle', 'motorcycle', 'backpack',
        'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'sports_ball',
        'baseball_bat', 'baseball_glove', 'tennis_racket', 'bottle',
        'wine_glass', 'cup', 'fork', 'knife', 'spoon', 'chair', 'couch',
        'laptop', 'mouse', 'remote', 'keyboard', 'cell_phone', 'book',
        'scissors', 'hair_drier', 'toothbrush',
        
        'weapon', 'handgun', 'rifle', 'shotgun',
    )