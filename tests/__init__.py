import logging
import os
import sys
import shutil
import tomli
from pathlib import Path

NAME = {{ cookiecutter.project_name }}
HOME = Path(os.path.expanduser("~"))
DESKTOP = HOME / "Desktop"

PROJECT_DIR = Path(os.path.abspath(__file__)).parent
FIG_DIR = PROJECT_DIR / "figs"
PUB_DIR = PROJECT_DIR / "writing" / "figs"
CONFIG_PATH = Path().home() / ".config" / NAME
CONFIG_FILE = CONFIG_PATH / "config.ini"
CONFIG_INI = PROJECT_DIR/ "config.ini"

### LOGGING ###
from logging.config import fileConfig

logging.getLogger("matplotlib").setLevel(logging.WARNING)
logging.getLogger("h5py").setLevel(logging.WARNING)

logging_conf = Path(PROJECT_DIR, "logging.conf")
fileConfig(logging_conf)

LOG = logging.getLogger(f"{{cookiecutter.project_name}}")

import coloredlogs

coloredlogs.install(
    level="DEBUG",
    fmt="%(asctime)s %(levelname)8s %(name)s.%(funcName)s >> %(message)s",
    datefmt="%H:%M:%S",
    stream=sys.stdout,
    logger=LOG,
    isatty=True,
)

LOG.info(f"WELCOME TO {NAME}")


make_configfile()
SETTINGS = load_config()