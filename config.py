from dataclasses import dataclass, field

@dataclass
class DatabaseConfig:
    database: str = ''         # Название базы данных
    db_host: str = ''          # URL-адрес базы данных
    db_user: str = ''          # Username пользователя базы данных
    db_password: str = ''      # Пароль к базе данных

@dataclass
class TgBot:
    token: str                     # Токен для доступа к телеграм-боту
    admin_ids: list[int]           # Список id администраторов бота



@dataclass
class Config:
    tg_bot: TgBot       # Используем default_factory для создания нового экземпляра TgBot
    db: DatabaseConfig  # Используем default_factory для создания нового экземпляра DatabaseConfig

#создаем экземпляр класса Config и заполняем его данными
config_my = Config(
    tg_bot=TgBot(
        token='6569223303:AAG36G9purad2ohDzXuYrFiba8vvp6Z7mqM',
        admin_ids=[544595769] # Если хочешь поменять на свой айди помений последнюю цифру на 8 
    ),
    db=DatabaseConfig(
        database='',
        db_host='',
        db_user='',
        db_password=''
    )
)