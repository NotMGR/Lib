from pydantic import BaseModel, ConfigDict

class UserResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    is_active: bool

class UserCreate(BaseModel):
    username: str
    is_active: bool

class NikkeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    image_path: str

class RaidResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str

class BossResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    raid_id: int
    weakness: str

class RaidInfoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    bosses: list[BossResponse]

class BossUpdate(BaseModel):

    id: int
    name: str
    weakness: str

class BossCreate(BaseModel):
    name: str
    weakness: str

class RaidCreate(BaseModel):

    name: str
    bosses: list[BossCreate]

class RaidUpdate(BaseModel):
    model_config = ConfigDict()

    name: str
    bosses: list[BossUpdate]

class MockResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: str
    damage_number: int
    boss_id: int
    images:list[str]
    mock_id: int
    is_active: bool

class RankResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    rank: int   
    username: str
    damage: int
    is_active: bool

class BossRankingReponse(BaseModel):
    average: float | None
    rankings: list[RankResponse]

class NikkeResponse(BaseModel):
    id: int
    name: str
    element: str
    manufacturer: str
    burst: int
    role: str
    image_path: str

class NikkeCreate(BaseModel):
    name: str
    element: str
    manufacturer: str
    burst: int
    role: str
    image_path: str

class AttemptResponse(BaseModel):
    id: int
    user_id: int
    raid_id: int
    username: str
    attempts: list[bool]
    attempts_remaining: int

class AttemptUpdate(BaseModel):
    active_buttons: list[int]

class UserMini(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str

class BossMini(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    weakness: str

class NikkeMini(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    image_path: str

class TeamMini(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int

class TeamCharacterResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nikke: NikkeMini

class TeamResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    team_order: str

class MockDetailsResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    damage_number: int
    is_active: bool

    player: UserMini
    boss: BossMini
    team: TeamResponse | None = None

class MockUpdate(BaseModel):
    damage_number: int
    team_members: list[int] | None = None

class MockCreate(BaseModel):
    damage_number: int
    player_id: int
    boss_id: int
    team_members: list[int] | None = None

class MockActiveUpdate(BaseModel):
    is_active: bool