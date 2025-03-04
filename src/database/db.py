import json


def json_dump(data: dict):
    try:
        with open("src/database/users.json", "w") as f:
            json.dump(data, f)

    except Exception as e:
        print(e)


def json_loads():
    try:
        with open("src/database/users.json") as f:
            content = f.read()
            return json.loads(content)
    except Exception as e:
        print(e)


def add_user_to_db(user_id: str):
    template = json_loads()
    if user_id not in template["users"]:
        template["users"].append(user_id)
        json_dump(template)


def get_users_list():
    template = json_loads()
    return template["users"]
