import bcrypt


def generate_password_hash(password: str) -> str:
    """
    Gera um hash seguro para uma senha fornecida usando a biblioteca bcrypt.

    Args:
        password (str): A senha que será convertida em hash.

    Returns:
        str: O hash da senha, codificado como uma string.

    Raises:
        ValueError: Se a senha for nula ou inválida.
    """
    if not password or not isinstance(password, str):
        raise ValueError("A senha deve ser uma string não vazia.")

    try:
        # Gera um salt aleatório e aplica o hash
        salt = bcrypt.gensalt(14)
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")
    except Exception as e:
        raise RuntimeError(f"Erro ao gerar o hash da senha: {e}")


def check_password(password: str, hashed_password: str) -> bool:
    """
    Verifica se a senha fornecida corresponde ao hash armazenado.

    Args:
        password (str): Senha fornecida.
        hashed_password (str): Hash armazenado no banco.

    Returns:
        bool: True se a senha for válida, False caso contrário.
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
