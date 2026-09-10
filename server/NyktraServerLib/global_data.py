from dataclasses import dataclass, field
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
databases_dir = Path(__file__).resolve().parent.parent / "databases"

@dataclass
class User:
  name: str
  username: str
  password_hash: str

  def __str__(self):
    return f"User:\n  name: {self.name}\n  username: {self.username}\n  password_hash: {self.password_hash}"

  def __repr__(self):
    return f"User(name={self.name!r}, username={self.username!r}, password_hash={self.password_hash!r})"

@dataclass
class Group:
  name: str
  password_required: bool = True
  users_limit: int = 0
  members: list[str] = field(default_factory=list)

  def __str__(self):
    return f"Group:\n  name: {self.name}\n  password required: {self.password_required}\n  users limit: {self.users_limit}\n  members: {self.members}"

  def __repr__(self):
    return f"Group(name={self.name!r}, password_required={self.password_required}, users_limit={self.users_limit}, members={self.members})"

  def __len__(self):
    return len(self.members)

  def __getitem__(self, key):
    return self.members[key]

@dataclass
class Command:
  code: str
  return_value: bool

  def __str__(self):
    return self.code

  def __repr__(self):
    return f"Command(code={self.code!r}, return_value={self.return_value})"