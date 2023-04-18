from aiogram import executor
from admin.handlers import admin
from handlers.users.help import register_handler_help
from loader import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)
admin.register_handler_admin(dp)
register_handler_help(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

