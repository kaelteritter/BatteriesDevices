from os import getenv

from dotenv import find_dotenv, load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

load_dotenv(find_dotenv())


DB_NAME = getenv('DB_NAME')
DB_PORT = getenv('DB_PORT')
DB_HOST = getenv('DB_HOST')
DB_USER = getenv('DB_USER')
DB_PASSWORD = getenv('DB_PASSWORD')

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(
    DATABASE_URL,
    echo=False
)

async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_db():
    async with async_session() as session:
        yield session