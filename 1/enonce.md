# 🕒 Time Spent Connected

## 🧠 Énoncé

Vous disposez d'une liste de journaux de connexion contenant des événements de type **login** ou **logout** pour différents utilisateurs. Chaque entrée est composée d’un horodatage (format ISO 8601), d’un identifiant utilisateur et d’une action.

L’objectif est de calculer le **temps total passé connecté** pour chaque utilisateur.

### Format des données :

Chaque entrée dans les logs suit la structure suivante :

```python
(timestamp, user_id, action)
```

- `timestamp` : chaîne ISO 8601 (ex : `"2023-10-21T10:00:00Z"`)
- `user_id` : identifiant unique de l'utilisateur (ex : `"user123"`)
- `action` : `"login"` ou `"logout"`

### Exemple :

```python
logs = [
    ("2023-10-21T10:00:00Z", "alice", "login"),
    ("2023-10-21T10:30:00Z", "alice", "logout"),
    ("2023-10-21T11:00:00Z", "bob", "login"),
    ("2023-10-21T11:45:00Z", "bob", "logout"),
]
```

Résultat attendu :

```python
{
    "alice": 1800.0,
    "bob": 2700.0
}
```

Les temps sont exprimés en secondes.

---

## 🛠️ Astuces

- Utilisez le module `datetime` pour convertir les timestamps ISO 8601 en secondes.
- Gardez une trace des heures de connexion (`login`) dans un dictionnaire.
- Lors d’un `logout`, calculez la durée connectée en soustrayant l’heure de `login`.
- Attention :
  - Un utilisateur peut se connecter plusieurs fois.
  - Il peut y avoir des **anomalies** comme :
    - Un `logout` sans `login` préalable.
    - Un `login` sans `logout` correspondant.
- Gérer ces cas avec des messages d'avertissement (`print`).