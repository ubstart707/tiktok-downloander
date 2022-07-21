from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5586348698:AAE0PjwxjctWS3nE9qzHf2E8JfllZPAAn6Y"  # Bot toekn
ADMINS = [1845028912] # adminlar ro'yxati
#IP = env.str("ip")  # Xosting ip manzili
