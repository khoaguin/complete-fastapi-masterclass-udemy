from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def bcrypt(password: str):
        """
        Hashing a password with bcrypt
        """
        return pwd_ctx.hash(password)

    def verify(hashed_password, plain_password):
        """
        Verify if the hashed plain_pasword matches the hashed_password
        """
        return pwd_ctx.verify(plain_password, hashed_password)
