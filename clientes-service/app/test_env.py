from .config import Config

cfg = Config()

print("MYSQL_USER:", cfg.MYSQL_USER)
print("MYSQL_PASSWORD:", cfg.MYSQL_PASSWORD)
print("MYSQL_HOST:", cfg.MYSQL_HOST)
print("MYSQL_DB:", cfg.MYSQL_DB)
