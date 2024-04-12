import asyncio
from aiogram import Bot, Dispatcher
import admin_handlers
import user_handlers
from config import config_my

#функция конфигурирования и запуска бота
async def main():

    #регистрируем бота и диспетчер
    bot = Bot(token=config_my.tg_bot.token)
    dp = Dispatcher()

    #регистрируем роутеры в диспетчер
    dp.include_router(admin_handlers.router)
    dp.include_router(user_handlers.router)

    #пропускаем накопившиемя апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    print('Запуск прошел успешно')
    asyncio.run(main())
