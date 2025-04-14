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
















def run_tests():
    test_cases = [
        (
            # Cas standard avec connexions et déconnexions bien appariées
            [
                ("2025-04-08T10:00:00Z", "user_1", "login"),
                ("2025-04-08T10:05:00Z", "user_2", "login"),
                ("2025-04-08T10:15:00Z", "user_1", "logout"),
                ("2025-04-08T10:20:00Z", "user_2", "logout"),
                ("2025-04-08T10:30:00Z", "user_1", "login"),
                ("2025-04-08T10:45:00Z", "user_1", "logout"),
            ],
            {
                "user_1": 15 * 60 + 15 * 60,  # 30 min total
                "user_2": 15 * 60
            }
        ),
        (
            # Cas avec logout sans login
            [
                ("2025-04-08T10:15:00Z", "user_1", "logout"),
            ],
            {}
        ),
        (
            # Cas avec login sans logout
            [
                ("2025-04-08T10:00:00Z", "user_1", "login"),
            ],
            {}
        ),
        (
            # Cas vide
            [],
            {}
        )
    ]

    for i, (logs, expected) in enumerate(test_cases, 1):
        print(f"--- Test {i} ---")
        try:
            result = time_spent_connected(logs)
            # Comparaison avec tolérance d'arrondi
            all_close = all(abs(result.get(k, 0) - v) < 1 for k, v in expected.items()) and len(result) == len(expected)
            assert all_close, f"Échec: attendu {expected}, obtenu {result}"
            print(f"✅ Test {i} OK")
        except AssertionError as e:
            print("❌", e)
        except Exception as e:
            print(f"⚠️ Erreur inattendue dans le test {i} :", e)
        print()

run_tests()
