import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

import os

os.system("python detect.py --weights models/best.pt --img 416 --conf 0.1 --source 0")
# python detect.py --weights runs/train/yolov5s_results/weights/best.pt --img 416 --conf 0.1 --source '/content/Sign_language_data/test/images