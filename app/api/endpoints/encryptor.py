# import passlib for password encryption
from passlib.context import CryptContext

# hashing context
passwordHashContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


# returns hashed password from plaintext password
def hashPassword(password: str) -> str:
    return passwordHashContext.hash(password)


def compareHash(plaintext: str, hashpass: str) -> bool:
    return passwordHashContext.verify(plaintext, hashpass)
