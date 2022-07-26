from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class DiscordUser(Base):
    __tablename__ = "discord_user"

    id = Column(Integer, primary_key=True)
    username = Column(String(64))
    validator = relationship("Validator", back_populates="validator")
    nominator = relationship("Nominator", back_populates="nominator")

    def __repr__(self):
        return f"DiscordUser(id={self.id!r}, username={self.name!r})"


class Validator(Base):
    __tablename__ = "validator"

    id = Column(Integer, primary_key=True)
    address = Column(String(64))
    discord_user_id = Column(Integer, ForeignKey("discord_user.id", ondelete='SET NULL'), nullable=True)
    discord_user = relationship("DiscordUser", back_populates="validator", uselist=False)

    def __repr__(self):
        return f"Validator(id={self.id!r}, address={self.address!r})"


class Nominator(Base):
    __tablename__ = "nominator"

    id = Column(Integer, primary_key=True)
    address = Column(String(64))
    discord_user_id = Column(Integer, ForeignKey("discord_user.id", ondelete='SET NULL'), nullable=True)
    discord_user = relationship("DiscordUser", back_populates="nominator", uselist=False)

    def __repr__(self):
        return f"Nominator(id={self.id!r}, address={self.address!r})"
