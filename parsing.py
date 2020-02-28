# directory_search.py ==> hcc_image_annotation
import os
import sys
import xml.etree.ElementTree as etree
xmlp = etree.XMLParser(encoding="utf-8")

dataset_path = "C:/Users/user/Desktop"

IMAGE_FOLDER = "C:/Users/user/Desktop/hcc_bounded_image"
ANNOTATIONS_FOLDER = "C:/Users/user/Desktop/hcc_bounded_annotation"
# ann_root, ann_dir, ann_files = next(os.walk(os.path.join(dataset_path, ANNOTATIONS_FOLDER)))
# print(ann_root)
# print("ROOT : {}\n".format(ann_root))
# print("DIR : {}\n".format(ann_dir))
# print("FILES : {}\n".format(ann_files))

xmID = etree.parse("C:/Users/user/Desktop/hcc_bounded_annotation/1001.xml",parser=xmlp)
root = xmID.getroot()

etree.dump(xmID)

1702 1989 7046