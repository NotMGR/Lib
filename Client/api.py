import requests
from settings import get_base_url, load_config


def fetch_raids(union_id):
    try:
        response = requests.get(
            f"{get_base_url()}/raids/",
            params={"union_id": union_id}
            ,timeout=5
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return None


def fetch_mock_info(raid_id):
    response = requests.get(
        f"{get_base_url()}/mocks",
        params={"raid_id": raid_id}
        )
    
    response.raise_for_status()
    return response.json()

def fetch_mock(mock_id):
    response = requests.get(
        f"{get_base_url()}/mocks/{mock_id}"
    )
    response.raise_for_status()
    return response.json()
    
def fetch_raid_boss_info(raid_id):
    response = requests.get(
        f"{get_base_url()}/boss",
        params={"raid_id": raid_id}
    )
    response.raise_for_status()
    return response.json()

def fetch_ranking(raid_id, include_inactive):
    response = requests.get(
        f"{get_base_url()}/ranking",
        params = {
            "raid_id": raid_id,
            "include_inactive": include_inactive
        }
    )
    response.raise_for_status()
    return response.json()

def fetch_raid_info(raid_id):
    response = requests.get(f"{get_base_url()}/raids/{raid_id}",)
    response.raise_for_status()
    return response.json()

def fetch_users(union_id=None):
    try:
        params = {}

        if union_id is not None:
            params["union_id"] = union_id

        response = requests.get(
            f"{get_base_url()}/users/",
            params=params,
            timeout=5
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException:
        return None


def fetch_user(user_id):
    response = requests.get(f"{get_base_url()}/{user_id}")
    response.raise_for_status()
    return response.json()

def create_user(user_data):
    response = requests.post(f"{get_base_url()}/users",
                            json=user_data)
    response.raise_for_status()
    return response.json()

def update_user(user_id, user_data):
    response = requests.put(f"{get_base_url()}/users/{user_id}", json=user_data)
    response.raise_for_status()
    return response.json()

def fetch_nikkes():
    response = requests.get(f"{get_base_url()}/nikkes")
    response.raise_for_status()
    return response.json()

def fetch_nikke(nikke_id):
    response = requests.get(f"{get_base_url()}/nikkes/{nikke_id}")
    response.raise_for_status()
    return response.json()

def create_nikke(nikke_data):
    response = requests.post(
        f"{get_base_url()}/nikkes",
        json=nikke_data
    )
    response.raise_for_status()
    return response.json()

def delete_nikke(nikke_id):
    response = requests.delete(f"{get_base_url()}/nikkes/{nikke_id}")
    response.raise_for_status()
    return response.json()

def update_nikke(nikke_id, nikke_data):
    response = requests.put(f"{get_base_url()}/nikkes/{nikke_id}", json=nikke_data)
    response.raise_for_status()
    return response.json()

def fetch_attempts(raid_id):
    response = requests.get(f"{get_base_url()}/attempts/{raid_id}")
    response.raise_for_status()
    return response.json()

def update_attempt(attempt_id, active_buttons):
    response = requests.put(f"{get_base_url()}/attempts/{attempt_id}", json={"active_buttons": active_buttons})
    response.raise_for_status()
    return response.json()

def toggle_user_mocks(raid_id, user_id):
    response = requests.put(f"{get_base_url()}/mocks/toggle/{raid_id}/{user_id}")
    response.raise_for_status()
    return response.json()

def toggle_1_user_mock(mock_id, is_active):
    response = requests.put(f"{get_base_url()}/mocks/{mock_id}/active", json={"is_active": is_active})
    if not response.ok:
        print(response.text)
    response.raise_for_status()
    return response.json()

def update_raid(raid_id, raid_info):
    response = requests.put(f"{get_base_url()}/raids/{raid_id}", json=raid_info)
    response.raise_for_status()
    return response.json()

def create_raid(raid_data):
    response = requests.post(f"{get_base_url()}/raids/", json=raid_data)
    response.raise_for_status()
    return response.json()

def update_mock_info(mock_id, mock_data):
    response = requests.put(f"{get_base_url()}/mocks/{mock_id}", json=mock_data)
    response.raise_for_status()
    return response.json()

def delete_mock(mock_id):
    response = requests.delete(f"{get_base_url()}/mocks/{mock_id}")
    response.raise_for_status()
    return response.json()

def create_mock(mock_data):
    response = requests.post(f"{get_base_url()}/mocks/", json=mock_data)
    response.raise_for_status()
    return response.json()

def delete_raid(raid_id):
    response = requests.delete(f"{get_base_url()}/raids/{raid_id}")
    response.raise_for_status()
    return response.json()

def upload_nikke_image(file_path):
    with open(file_path, "rb") as f:
        response = requests.post(
            f"{get_base_url()}/images/nikke",
            files={
                "image": f
            }
        )

    response.raise_for_status()
    return response.json()

def fetch_unions():
    response = requests.get(f"{get_base_url()}/unions")
    response.raise_for_status()
    return response.json()

def fetch_union(union_id):
    response = requests.get(f"{get_base_url()}/unions/{union_id}")
    response.raise_for_status()
    return response.json()

def create_union(union_data):
    response = requests.post(f"{get_base_url()}/unions", json=union_data)
    response.raise_for_status()
    return response.json()

def update_union(union_id, union_data):
    response = requests.put(f"{get_base_url()}/unions/{union_id}", json=union_data)
    response.raise_for_status()
    return response.json()

def get_base_url():
    config = load_config()
    return config.get("server", "").rstrip("/")

def test_server_connection(server_url):
    if not server_url:
        return False

    try:
        response = requests.get(
            f"{server_url}/",
            timeout=5
        )
        response.raise_for_status()

        return response.json().get("status") == "Backend is running"

    except (requests.RequestException, ValueError):
        return False
    

def handle_api_error(e):
    status = e.response.status_code

    messages = {
        400: "Invalid request.",
        404: "Item not found.",
        409: "This item already exists.",
        422: "Invalid information provided",
        500: "Internal server error."
    }

    return messages.get(status, "Something went wrong.")

def get_auth():
    config = load_config()

    return(
        config["username"],
        config["password"]
    )