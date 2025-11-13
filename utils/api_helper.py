import requests

BASE_URL = "https://conduit-api.bondaracademy.com/api"


def get_user_token(email, password):
    # Log in and return the user's authentication token.

    url = f"{BASE_URL}/users/login"
    payload = {"user": {"email": email, "password": password}}
    res = requests.post(url, json=payload)
    res.raise_for_status()
    return res.json()["user"]["token"]


def create_article(token, title, description, body, tags):
    # Create a new article using the Conduit API.
    url = f"{BASE_URL}/articles"
    headers = {"Authorization": f"Token {token}"}
    payload = {
        "article": {
            "title": title,
            "description": description,
            "body": body,
            "tagList": tags,
        }
    }
    res = requests.post(url, json=payload, headers=headers)
    res.raise_for_status()
    return res.json()["article"]
