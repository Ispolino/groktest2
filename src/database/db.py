import json


def json_dump(data: dict):
    with open("src/database/users.json", "w") as f:
        json.dump(data, f)


def json_loads():
    with open("src/database/users.json") as f:
        content = f.read()
        return json.loads(content)


def add_user_to_db(user_id: int):
    template = json_loads()
    if user_id not in template["users"]:
        template["users"].append(str(user_id))
        json_dump(template)


def get_users_list():
    template = json_loads()
    return template["users"]
