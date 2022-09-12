from __future__ import absolute_import

import logging
import os
import shutil
import sys
from pathlib import Path

import coloredlogs
import matplotlib as mpl
import tomli

PROJECT_DIR = Path(os.path.abspath(__file__)).parent
FIG_DIR = PROJECT_DIR / "figs"
PUB_DIR = PROJECT_DIR / "writing" / "figs"
HOME = Path(os.path.expanduser("~"))
DESKTOP = HOME / "Desktop"

CONFIG_PATH = Path().home() / ".config" / "QDM_ML"
CONFIG_FILE = CONFIG_PATH / "config.ini"
CONFIG_INI = PROJECT_DIR / "config.ini"
