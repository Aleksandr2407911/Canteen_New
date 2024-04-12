from dataclasses import dataclass

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
        token='6982700202:AAGHvIHctbf2rPdXeOFcQKXUWjpHTs8aoG4',
        admin_ids=[544595768]
    ),
    db=DatabaseConfig(
        database='',
        db_host='',
        db_user='',
        db_password=''
    )
)
