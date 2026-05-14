import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

load_dotenv()


# Neon DB URL 가져오기

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set. Check your .env file.")


# 비동기 엔진 생성

engine = create_async_engine(DATABASE_URL, echo=True)


# 세션 팩토리 생성

AsyncSessionLocal = async_sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False,
)

Base = declarative_base()


# Dependency: DB 세션 주입


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
