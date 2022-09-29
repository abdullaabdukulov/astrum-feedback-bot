from aiogram import executor

from handlers.users.telegram_bots.handlers import admin
from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)
admin.register_handler_admin(dp)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
