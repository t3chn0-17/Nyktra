# import asyncio
import aiosqlite as sql
from .global_data import databases_dir, Command

class DBController:
  def __init__(
      self, name: str, db_file_name: str,
      db, connection_state: bool = False,
    ):
    self.name = name
    self.db_file_name = db_file_name
    self.db = db
    self.connection_state = connection_state

  @classmethod
  async def connect(cls, name: str, db_file_name: str):
    db = await sql.connect(f"{databases_dir}\\{db_file_name}")
    return cls(
      name, db_file_name, db, True
    )

  async def execute(self, command: Command):
    cursor = await self.db.execute(command.code)

    if command.return_value:
      result = await cursor.fetchall()
      await cursor.close()
      return result

    await self.db.commit()
    await cursor.close()

  async def close(self):
    if self.db:
      await self.db.close()
      self.connection_state = False