from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        # User   → "users"
        # Brand  → "brands"
        # Automatically lowercases class name and adds "s"
        return cls.__name__.lower() + "s"

    

