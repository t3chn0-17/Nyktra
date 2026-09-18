from rich.console import Console
from pathlib import Path

console = Console()

db_dir = Path(__file__).parent.parent / "databases"
sounds_dir = Path(__file__).parent.parent / "sounds"

def ensure_dirs() -> None:
  db_dir.mkdir(parents=True, exist_ok=True)
  sounds_dir.mkdir(parents=True, exist_ok=True)