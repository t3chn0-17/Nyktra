from pygame import mixer
from ..config import sounds_dir

mixer.init()

sounds = {
  "click": mixer.Sound(sounds_dir / "click.wav"),
  "select": mixer.Sound(sounds_dir / "select.wav"),
  "error": mixer.Sound(sounds_dir / "error.wav"),
  "message": mixer.Sound(sounds_dir / "message.wav"),
}