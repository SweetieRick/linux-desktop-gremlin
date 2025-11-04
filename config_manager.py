
import os
import settings
from flask import json


def load_master_config():
    """ Loads the main config.json file. """
    path = os.path.join(settings.BASE_DIR, "config.json")
    if not os.path.exists(path):
        print(f"Warning: Master config file not found at {path}")
        return

    s = settings.Settings
    with open(path, 'r') as f:
        data = json.load(f)
        for key, val in data.items():
            if hasattr(s, key):
                setattr(s, key, val)


def load_config_char():
    """ Loads the character-specific config.json file. """
    path = os.path.join(
        settings.BASE_DIR,
        "SpriteSheet", "Gremlins", settings.Settings.StartingChar, "config.json"
    )
    if not os.path.exists(path):
        print(f"Warning: Character config file not found at {path}")
        return

    f = settings.FrameCounts
    with open(path, 'r') as f_char:
        data = json.load(f_char)
        for key, val in data.items():
            if hasattr(f, key):
                setattr(f, key, val)
        # override frame rate if specified
        if 'FrameRate' in data:
            settings.Settings.FrameRate = data['FrameRate']
