from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

def verify_password(hashed_password: str, raw_password: str):
  ph = PasswordHasher()
  try:
    ph.verify(hashed_password, raw_password)
    return True
  except VerifyMismatchError:
    return False