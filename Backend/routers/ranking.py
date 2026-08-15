from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload

from auth import authenticate
from database import get_db
from models import Boss, MockDamage, User
from schemas import RankResponse, BossRankingReponse

router = APIRouter(
    prefix="/ranking",
    tags=["Ranking"],
    dependencies=[Depends(authenticate)]
)

@router.get("/", response_model=dict[int, BossRankingReponse])
def get_ranking(raid_id: int, include_inactive: bool, db: Session = Depends(get_db)):

    query = (db.query(
                    MockDamage.id,
                    MockDamage.boss_targeted,
                    MockDamage.damage_number,
                    User.username,
                    MockDamage.is_active
                )
                .join(User, User.id == MockDamage.player_id)
                .join(Boss, Boss.id == MockDamage.boss_targeted)
                .filter(Boss.raid_id == raid_id)
    )   
    
    if not include_inactive:
        query = query.filter(MockDamage.is_active == True)
    
    mock_list = query.all()

    return build_ranking_response(mock_list)

def build_ranking_response(mocks):
    grouped_mocks = {}

    ranking_response = {}

    #Group by boss
    for mock in (mocks):
        grouped_mocks.setdefault(mock.boss_targeted, []).append(mock)

    for boss_id, boss_mocks in grouped_mocks.items():
        boss_mocks.sort(
            key=lambda mock: mock.damage_number,
            reverse=True
        )

        #Calculate the average
        average = (
            sum(mock.damage_number for mock in boss_mocks)/len(boss_mocks)
            if boss_mocks
            else None
        )

        #Create the boss entry
        ranking_response[boss_id] = {
            "average": average,
            "rankings": []
        }

        #build ranking list
        for rank, mock in enumerate(boss_mocks, start=1):
            ranking_response[boss_id]["rankings"].append({
                "id": mock.id,
                "rank": rank,
                "username": mock.username,
                "damage": mock.damage_number,
                "is_active":mock.is_active
            })

    return ranking_response
