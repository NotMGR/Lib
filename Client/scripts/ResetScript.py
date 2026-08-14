from database.db_manager import Session, MockDamage, DamageDone, AttemptFrameTable, Boss, Raid, TeamCharacter, Team, User

with Session() as session:
    session.query(Raid).delete()
    session.query(User).delete()

    session.commit()

print("Database reset complete.")