from sqlalchemy import create_engine, Boolean, Column, Integer, String, ForeignKey, DateTime, BigInteger
from sqlalchemy.orm import relationship, sessionmaker, Mapped, mapped_column
from pathlib import Path
from database import Base

from datetime import datetime

#Defining the tables as classes

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime)
    is_active = Column(
    Boolean,
    default=True,
    nullable=False
)

    union_id = Column(
        Integer,
        ForeignKey("unions.id"),
        nullable=False
    )

    union = relationship(
        "Union",
        back_populates="users"
    )

    damages = relationship("DamageDone", back_populates="player")
    mock_damages = relationship("MockDamage", back_populates="player")
    attempts = relationship(
        "AttemptFrameTable",
        back_populates="user",
        cascade="all, delete-orphan"
    )

class Nikke(Base):
    __tablename__ = "nikkes"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    burst = Column(Integer)
    element = Column(String)
    manufacturer = Column(String)
    role = Column(String)
    image_path = Column(String)

class Raid(Base):
    __tablename__ = "raid"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    union_id = Column(
        Integer,
        ForeignKey("unions.id"),
        nullable=False
    )

    union = relationship(
        "Union",
        back_populates="raids"
    )

    bosses = relationship(
        "Boss",
        back_populates="raid",
        cascade="all, delete-orphan"
    )

    raid_attempt = relationship(
        "AttemptFrameTable",
        back_populates="raids_att",
        cascade="all, delete-orphan"
    )


class Boss(Base):
    __tablename__ = "boss"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    weakness = Column(String, nullable=False)
    hp = Column(BigInteger)
    raid_id = Column(Integer, ForeignKey("raid.id"), nullable=False)

    raid = relationship("Raid", back_populates="bosses")
    damages = relationship("DamageDone", back_populates="boss")
    mock_damages = relationship("MockDamage", back_populates="boss", cascade="all, delete-orphan")

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    signature = Column(String, unique=True)
    team_order = Column(String)

    characters = relationship(
        "TeamCharacter",
        back_populates="team",
        cascade="all, delete-orphan"
    )

    damages = relationship("DamageDone", back_populates="team")
    mock_damages = relationship("MockDamage", back_populates="team")

class TeamCharacter(Base):
    __tablename__ = "team_characters"

    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    character_id = Column(Integer, ForeignKey("nikkes.id"))

    team = relationship("Team", back_populates="characters")
    nikke = relationship("Nikke")

class DamageDone(Base):
    __tablename__ = "damage_done"

    id = Column(Integer, primary_key=True)
    damage_number = Column(BigInteger, nullable=False)
    player_id = Column("player", Integer, ForeignKey("users.id"))
    boss_targeted = Column(Integer, ForeignKey("boss.id"))
    date = Column(DateTime)
    team_used = Column(Integer, ForeignKey("teams.id"))

    player = relationship("User", back_populates="damages")
    boss = relationship("Boss", back_populates="damages")
    team = relationship("Team", back_populates="damages")

class MockDamage(Base):
    __tablename__ = "mock_damage"
    
    id = Column(Integer, primary_key=True)
    damage_number = Column(BigInteger, nullable=False)
    player_id = Column(Integer, ForeignKey("users.id"))
    boss_targeted = Column(Integer, ForeignKey("boss.id"))
    date = Column(DateTime)
    team_used = Column(Integer, ForeignKey("teams.id"))
    is_active = Column(
    Boolean,
    default=True,
    nullable=False
)

    player = relationship("User", back_populates="mock_damages")
    boss = relationship("Boss", back_populates="mock_damages")
    team = relationship("Team", back_populates="mock_damages")

class AttemptFrameTable(Base):
    __tablename__ = "attempts_used"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    raid_id: Mapped[int] = mapped_column(
        ForeignKey("raid.id"),
        nullable=False
    )

    btn_1: Mapped[int] = mapped_column(nullable=False)
    btn_2: Mapped[int] = mapped_column(nullable=False)
    btn_3: Mapped[int] = mapped_column(nullable=False)
    btn_4: Mapped[int] = mapped_column(nullable=False)
    btn_5: Mapped[int] = mapped_column(nullable=False)

    attempts_remaining: Mapped[int] = mapped_column(nullable=False)

    user: Mapped["User"] = relationship(
        back_populates="attempts"
    )
    raids_att: Mapped["Raid"] = relationship(
        back_populates="raid_attempt"
    )

class Union(Base):
    __tablename__ = "unions"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    users = relationship(
        "User",
        back_populates="union",
        cascade="all, delete-orphan"
    )

    raids = relationship(
        "Raid",
        back_populates="union",
        cascade="all, delete-orphan"
    )
