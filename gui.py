#!/bin/python3
import os
import sys
base_path = os.path.dirname(__file__)
sys.path.append(f'{base_path}/src')
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from windows import main
from cfg import global_variables as g


if __name__ == "__main__":
    g.init(base_path)
    pygame.mixer.init()
    main.init()
