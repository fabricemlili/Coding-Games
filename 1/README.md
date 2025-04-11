# Analyse de Logs Web

### 🧩 Enoncé

Tu travailles pour une entreprise de e-commerce, et on te donne un fichier de logs représentant des connexions utilisateurs. Chaque ligne du log est de la forme :

```
<timestamp> <user_id> <action>
```

### ✅ Exemples

```python
logs = [
    ("2025-04-08T10:00:00Z", "user_1", "login"),
    ("2025-04-08T10:05:00Z", "user_2", "login"),
    ("2025-04-08T10:15:00Z", "user_1", "logout"),
    ("2025-04-08T10:20:00Z", "user_2", "logout"),
    ("2025-04-08T10:30:00Z", "user_1", "login"),
    ("2025-04-08T10:45:00Z", "user_1", "logout"),
]
```

### 🎯 Objectif
Écris un programme Python qui :

1) Parse les logs.

2) Calcule le temps total passé connecté par chaque utilisateur (entre login et logout).

3) Retourne un dictionnaire Python du type :

```python
{
'user_1': 1800.0,  # en secondes
'user_2': 900.0
}
```
### 🧠 Astuce

Pour résoudre ce problème, tu peux suivre ces étapes :

1) Organisation des données

Trie les logs par timestamp pour t'assurer que les actions sont bien dans l'ordre chronologique.

2) Gestion des sessions utilisateur

Utilise un dictionnaire temporaire pour mémoriser l’heure de connexion (`login`) de chaque utilisateur en attente d’un `logout`.

3) Calcul du temps de session

Lorsqu’un `logout` est rencontré, calcule la différence entre le moment du `logout` et le `login` correspondant. Additionne cette durée au total pour cet utilisateur.

4) Conversion des timestamps

Utilise le module `datetime` pour convertir les timestamps ISO 8601 en objets `datetime` et faciliter les calculs de durée.

5) Retourner le résultat

Une fois tous les logs traités, retourne un dictionnaire contenant le temps total passé en ligne par chaque utilisateur.

💡 Pense à gérer les cas où un `logout` n’a pas de `login` correspondant ou inversement, selon le niveau de robustesse attendu de ton code.