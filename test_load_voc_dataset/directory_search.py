import os
import sys

dataset_path = sys.argv[1]

IMAGE_FOLDER = "JPEGImages"
ANNOTATIONS_FOLDER = "Annotations"

ann_root, ann_dir, ann_files = next(os.walk(os.path.join(dataset_path, ANNOTATIONS_FOLDER)))

print("ROOT : {}\n".format(ann_root))
print("DIR : {}\n".format(ann_dir))
print("FILES : {}\n".format(ann_files))