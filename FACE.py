import pathlib
import cv2 
import os

cascade_path=pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
print(cascade_path)//print

