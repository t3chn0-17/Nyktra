import aiosqlite as sql
import asyncio
from dataclasses import dataclass, field
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent


class User:
  name: str
  username: str
  password: None

class Group:
  name: str
  password_required: bool = True
  users_limit: int = 0
  logged_in_users: list[User] = field(default_factory=list)

async def add_user_db(user: User): pass

async def add_group_db(group: Group): pass