import keyboard
import requests
import Token_reseter
import config
import time
access_token = config.access_token

def reset_access_token():
       return Token_reseter.main(config.client_id,config.client_secret,config.refresh_token)

def update_access_token_in_config(new_token, config_path="config.py"):
    lines = []
    with open(config_path, "r") as file:
        lines = file.readlines()

    with open(config_path, "w") as file:
        for line in lines:
            if line.startswith("access_token="):
                file.write(f'access_token="{new_token}"\n')
            else:
                file.write(line)

while True:

    if keyboard.is_pressed("f7") and keyboard.is_pressed("ctrl"):
        response = requests.post(
            "https://api.spotify.com/v1/me/player/previous",
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )
        print("request sent!", response.status_code)
        response_1st=str(response.status_code)[0]
        if response_1st == '4':
            access_token =reset_access_token()
            update_access_token_in_config(access_token)

    elif keyboard.is_pressed("f8") and keyboard.is_pressed("ctrl"):
        response = requests.post(
            "https://api.spotify.com/v1/me/player/next",
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )
        print("request sent!", response.status_code)
        response_1st=str(response.status_code)[0]
        if response_1st == '4':
            access_token = reset_access_token()
            update_access_token_in_config(access_token)
    time.sleep(0.05)

