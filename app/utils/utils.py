import bcrypt


def hash_password(password: str) -> str:
    # Gera um salt aleatório e hashea a senha
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Verifica se a senha fornecida corresponde à senha hasheada
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
