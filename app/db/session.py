from sqlalchemy import create_engine

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,   # sends "SELECT 1" before using a connection
                          # prevents "MySQL server has gone away" errors
    pool_size=10,         # 10 connections always kept alive in the pool
    max_overflow=20,      # up to 20 extra connections under heavy load

)