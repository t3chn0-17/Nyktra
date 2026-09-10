from .args import cli_args
from .global_data import databases_dir

__version__ = "1.0.0"
__author__ = "Abdelrahman Essam"
__all__ = ["cli_args"]

databases_dir.mkdir(parents=True, exist_ok=True)