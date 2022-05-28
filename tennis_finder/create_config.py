import os
import secrets
import string


def generate_secure_random_string(n: int) -> str:
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(n))


with open("tennis_finder/config.py", "w", encoding="utf-8") as f:
    f.write("PORT = 5555\n")
    f.write("DB_URL = \"postgresql+psycopg2://tennis:tennisPass@localhost:5432/tennis\"\n")
    f.write(f"SECRET_KEY = \"{generate_secure_random_string(32)}\"\n")
    f.write(f"salt = \"{generate_secure_random_string(32)}\"\n")
    f.write(f"salt1 = \"{generate_secure_random_string(32)}\"\n")
    f.write(f"salt2 = \"{generate_secure_random_string(32)}\"\n")