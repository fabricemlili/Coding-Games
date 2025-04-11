
from datetime import datetime

def time_spent_connected(logs):
    login_times = {}
    time_spent = {}

    for timestamp, user_id, action in logs:
        ts = datetime.fromisoformat(timestamp[:-1]).timestamp()

        if action == 'login':
            login_times[user_id] = ts

        elif action == 'logout':
            if user_id in login_times:
                duration = ts - login_times[user_id]
                time_spent[user_id] = time_spent.get(user_id, 0) + duration
                del login_times[user_id]
            else:
                print(f"[WARN] Logout sans login pour {user_id} à {timestamp}")

    for user in login_times:
        print(f"[WARN] Utilisateur {user} s'est connecté sans se déconnecter.")

    return time_spent



logs = [
    ("2025-04-08T10:00:00Z", "user_1", "login"),
    ("2025-04-08T10:05:00Z", "user_2", "login"),
    ("2025-04-08T10:15:00Z", "user_1", "logout"),
    ("2025-04-08T10:20:00Z", "user_2", "logout"),
    ("2025-04-08T10:30:00Z", "user_1", "login"),
    ("2025-04-08T10:45:00Z", "user_1", "logout"),
]


print(time_spent_connected(logs))