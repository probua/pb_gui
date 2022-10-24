import os
import sys

def resources(file):
    try: base_path = sys._MEIPASS
    except: base_path = os.path.abspath(".")
    base_path += "/res"

    path = os.path.join(base_path, file)
    return path