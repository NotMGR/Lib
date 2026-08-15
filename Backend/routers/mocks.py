from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
import datetime

from auth import authenticate
from database import get_db
from models import MockDamage, Raid, Boss, Team, TeamCharacter
from schemas import MockResponse, MockDetailsResponse, MockUpdate, MockCreate, MockActiveUpdate

router = APIRouter(
    prefix="/mocks",
    tags=["Mocks"],
    dependencies=[Depends(authenticate)]
)

@router.get("/", response_model=list[MockResponse])
def get_mocks(
    raid_id: int, 
    db: Session = Depends(get_db)
):
    mock_list = (db.query(MockDamage)
                .join(MockDamage.boss)
                .filter(Boss.raid_id == raid_id)
                .options(
                    joinedload(MockDamage.player),
                    joinedload(MockDamage.team)
                        .joinedload(Team.characters)
                        .joinedload(TeamCharacter.nikke)
                )
                .all()
)   
    return build_mock_response(mock_list)

@router.get("/{mock_id}", response_model=MockDetailsResponse)
def get_mock_details(mock_id: int, db: Session = Depends(get_db)):

    mock = (
        db.query(MockDamage)
        .options(
            joinedload(MockDamage.player),
            joinedload(MockDamage.boss),
            joinedload(MockDamage.team)
                .joinedload(Team.characters)
                .joinedload(TeamCharacter.nikke)
        )
        .filter(MockDamage.id == mock_id)
        .first()
    )

    return mock
        
@router.put("/toggle/{raid_id}/{user_id}")
def toggle_user_mocks(
    raid_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):
    mocks = (
                db.query(MockDamage)
                    .join(
                        Boss,
                        MockDamage.boss_targeted == Boss.id
                    )
                    .filter(
                        MockDamage.player_id == user_id,
                        Boss.raid_id == raid_id
                    )
                    .all()
                )

    if not mocks:
        raise HTTPException(
            status_code=404,
            detail="No mocks found."
        )

    all_inactive = all(mock.is_active == False for mock in mocks)
    
    new_state = True if all_inactive else False

    for mock in mocks:
        mock.is_active = new_state

    db.commit()

    return {
        "message":"Mocks Updated sucessfully.",
        "is_active": bool(new_state)
    }

@router.put("/{mock_id}")
def update_mock(
    mock_id: int,
    data: MockUpdate,
    db: Session = Depends(get_db)
):
    mock = db.get(MockDamage, mock_id)
    if mock is None:
        raise HTTPException(
            status_code=404,
            detail="Mock not found."
        )

    if data.team_members:
        team_id = check_team_exists(
            data.team_members,
            db
        )
    else:
        team_id = None

    mock.damage_number = data.damage_number
    mock.team_used = team_id

    db.commit()
    db.refresh(mock)

    return mock

@router.delete("/{mock_id}")
def delete_mock(mock_id: int, db: Session = Depends(get_db)):

    mock = db.get(MockDamage, mock_id)

    if mock is None:
        raise HTTPException(
            status_code=404,
            detail="Mock not found."
        )

    db.delete(mock)
    db.commit()
    return{
        "message": "Mock deleted successfully."
    }

@router.post("/")
def create_mocks(
    mocks: list[MockCreate],
    db: Session = Depends(get_db)
):
    for mock in mocks:
        if mock.team_members:
            team_id = check_team_exists(mock.team_members, db)
        else:
            team_id = None

        mock_entry = MockDamage(
            damage_number = mock.damage_number,
            player_id = mock.player_id,
            boss_targeted = mock.boss_id,
            date = datetime.datetime.now(),
            team_used = team_id,
            is_active = True
        )

        db.add(mock_entry)

    db.commit()

    return {
        "message": "Mocks created successfully."
    }

@router.put("/{mock_id}/active")
def update_mock_active(
    mock_id: int,
    data: MockActiveUpdate,
    db: Session = Depends(get_db)
):
    mock = db.get(MockDamage, mock_id)
    if mock is None:
        raise HTTPException(
            status_code=404,
            detail="Mock not found."
        )
    
    mock.is_active = data.is_active

    db.commit()
    db.refresh(mock)

    return {
        "message": "Mock updated. "
    }
        

def check_team_exists(sel_signature, db): 
    
    formation_order = ",".join(
        map(str, sel_signature)
    )

    canonical_signature = ",".join(
        map(str, sorted(sel_signature))
    )

    existing = (db.query(Team)
                .filter(
                    Team.signature == canonical_signature
                )
                .first()
    )

    if existing:
        existing.team_order = formation_order

        return existing.id
    
    new_team = Team(
        signature=canonical_signature,
        team_order=formation_order
    )
    
    db.add(new_team)

    db.flush()

    for nikke_id in sel_signature:
        link = TeamCharacter(
            team_id=new_team.id,
            character_id=int(nikke_id)
        )

        db.add(link)
    
    db.flush()

    return new_team.id

def build_mock_response(rows):
    response = []

    for row in rows:

        images = []

        if row.team:
            ordered_ids = [
                int(id_) for id_ in row.team.team_order.split(",")
            ]

            char_lookup = {
                char.character_id: char.nikke.image_path for char in row.team.characters
            }

            images = [
                char_lookup[nikke_id]
                for nikke_id in ordered_ids
                if nikke_id in char_lookup
            ]

        response.append({
            "username": row.player.username,
            "damage_number": row.damage_number,
            "boss_id": row.boss_targeted,
            "images": images,
            "mock_id": row.id,
            "is_active":row.is_active, 
        })
    
    return response
