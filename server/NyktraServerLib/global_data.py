from dataclasses import dataclass, field
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
databases_dir = Path(__file__).resolve().parent.parent / "databases"

@dataclass
class User:
  name: str
  username: str
  password: None

@dataclass
class Group:
  name: str
  password_required: bool = True
  users_limit: int = 0
  logged_in_users: list[User] = field(default_factory=list)

@dataclass
class Command:
  code: str
  return_value: bool