#!/bin/python3
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import sys
sys.path.append('src')

import pygame
from windows import main
from cfg import init_variables as iv


if __name__ == "__main__":
    iv.init()
    pygame.mixer.init()
    main.init()
