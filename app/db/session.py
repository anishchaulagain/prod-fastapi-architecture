from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,   # sends "SELECT 1" before using a connection
                          # prevents "MySQL server has gone away" errors
    pool_size=10,         # 10 connections always kept alive in the pool
    max_overflow=20,      # up to 20 extra connections under heavy load

)

# SessionLocal is a class (factory), not an instance
# Every call to SessionLocal() gives you a fresh session
SessionLocal = sessionmaker(
    autocommit=False,   # YOU call db.commit() — nothing commits silently
    autoflush=False,    # SQLAlchemy won't issue surprise SQL mid-request
    bind=engine
)