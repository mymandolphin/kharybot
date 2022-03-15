import json

data = {"token": "token goes here", "log_channel_id": 0, "moderator_role_id": 0}

with open("config.json", "w") as file:
    json.dump(data, file, indent = 4)

print("config.json generated.")