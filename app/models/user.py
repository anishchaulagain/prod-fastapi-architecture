from datetime import datetime

from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped

from app.db.base_class import Base


class User(Base):
    # primary_key=True     → this is the PK column
    # index=True           → creates a DB index for fast lookups
    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    # String(255)          → VARCHAR(255) in MySQL
    # unique=True          → DB-level UNIQUE constraint (catches race conditions)
    # index=True           → creates index so email lookups are fast (O(log n))
    # nullable=False       → NOT NULL in DB — email is required
    email: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False, index=True
    )

    password: Mapped[str] = mapped_column(
        String(255), nullable=False
    )

    # Default True — account is active on creation
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Default False — new users are not admins
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)

    # server_default=func.now() means MySQL sets this, not Python
    # This is safer: the DB clock is the source of truth
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    # onupdate=func.now() → MySQL automatically updates this on every UPDATE
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

