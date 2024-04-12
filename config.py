from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    database: str = ''         # Название базы данных
    db_host: str = ''          # URL-адрес базы данных
    db_user: str = ''          # Username пользователя базы данных
    db_password: str = ''      # Пароль к базе данных

@dataclass
class TgBot:
    token: str = '6569223303:AAG36G9purad2ohDzXuYrFiba8vvp6Z7mqM' # Токен для доступа к телеграм-боту
    admin_ids: list[int] = []                                         # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot = TgBot() # загружаю объкт класса TgBot
    db: DatabaseConfig = DatabaseConfig()