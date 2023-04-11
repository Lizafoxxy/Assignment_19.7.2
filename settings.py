# это способ прописать логин и пароль так, чтобы не раскрывать их всем. Сам логин и пароль прописываются
# в файле .env как переменные valid_emial и valid_password. А здесь они только вызываются.

import os
from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')