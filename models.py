from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class DiscordUser(Base):
    __tablename__ = "discord_user"

    id = Column(Integer, primary_key=True)
    username = Column(String(64))
    is_validator = Column(Boolean, default=False)
    is_nominator = Column(Boolean, default=False)

    def __repr__(self):
        return f"DiscordUser(id={self.id!r}, username={self.name!r})"


class Validator(Base):
    __tablename__ = "validator"

    id = Column(Integer, primary_key=True)
    address = Column(String(64))

    def __repr__(self):
        return f"Validator(id={self.id!r}, address={self.address!r})"


class Nominator(Base):
    __tablename__ = "nominator"

    id = Column(Integer, primary_key=True)
    address = Column(String(64))

    def __repr__(self):
        return f"Nominator(id={self.id!r}, address={self.address!r})"
