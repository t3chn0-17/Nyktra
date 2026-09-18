from pygame import mixer
from ..config import sounds_dir

sounds = {}

def init_sounds() -> None:
  mixer.init()

  sounds.update({
    "click": mixer.Sound(sounds_dir / "click.wav"),
    "select": mixer.Sound(sounds_dir / "select.wav"),
    "error": mixer.Sound(sounds_dir / "error.wav"),
    "message": mixer.Sound(sounds_dir / "message.wav"),
  })