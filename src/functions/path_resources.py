import os
import sys
from cfg import global_variables as g


def resources(file):
    try: res_path = sys._MEIPASS
    except: res_path = g.APP_PATH
    res_path += "/res"

    path = os.path.join(res_path, file)
    return path
