import tomli
import shutil
import logging

from {{cookiecutter.project_name}} import CONFIG_FILE, CONFIG_INI, CONFIG_PATH

LOG = logging.getLogger({{cookiecutter.project_name}})
NAME = {{cookiecutter.project_name}}

def load_config():
    """
    Loads the config file.

    :return: dict
        config file
    """
    with open(CONFIG_FILE, "rb") as fileObj:
        return tomli.load(fileObj)

def make_configfile(reset=False):
    """
    Creates the config file if it does not exist.
    """
    CONFIG_PATH.mkdir(parents=True, exist_ok=True)
    if not CONFIG_FILE.exists() or reset:
        LOG.info(f"Copying default {{{cookiecutter.project_name}}} 'config.ini' file to {CONFIG_FILE}")
        shutil.copy2(CONFIG_INI, CONFIG_FILE)