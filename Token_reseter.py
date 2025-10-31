import requests
import base64
import config

def main(client_id, client_secret, refresh_token):
    # Encode client_id and client_secret for Basic Auth
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    # Request a new access token
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={
            "Authorization": f"Basic {auth_header}",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data={
            "grant_type": "refresh_token",
            "refresh_token": config.refresh_token
        }
    )

    if response.status_code != 200:
        raise Exception(f"Token refresh failed: {response.status_code} {response.text}")

    tokens = response.json()
    return tokens["access_token"]