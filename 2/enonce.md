# 📏 Longest Subarray with Sum K

## 🧠 Énoncé

Étant donné un tableau d'entiers `nums` et un entier `k`, votre objectif est de trouver la **longueur du plus long sous-tableau contigu** dont la somme est égale à `k`.

### Exemple :

```python
nums = [1, -1, 5, -2, 3]
k = 3
```

Le sous-tableau `[1, -1, 5, -2]` a une somme de `3` et une longueur de `4`, ce qui est le maximum possible ici.

**Résultat attendu :** `4`

---

## 🔍 Explication de l'algorithme

On utilise la technique de **somme cumulative** (`cumulative_sum`) combinée à un dictionnaire (`sum_index_map`) pour optimiser la recherche du sous-tableau en temps linéaire **O(n)**.

### Étapes principales :

1. **Initialisation :**
   - `cumulative_sum` pour stocker la somme courante.
   - `sum_index_map` pour mémoriser la **première occurrence** de chaque somme cumulative.
   - `max_length` pour suivre la plus grande longueur rencontrée.

2. **Itération sur les éléments du tableau :**
   - Ajouter l’élément courant à `cumulative_sum`.
   - Trois cas sont traités :
     - ✅ `cumulative_sum == k` → le sous-tableau commence à l'indice 0.
     - ✅ `cumulative_sum - k` a déjà été vu → il existe un sous-tableau de somme `k`.
     - ✅ On stocke `cumulative_sum` dans `sum_index_map` s’il n’a pas encore été vu, pour capturer la **plus ancienne occurrence** et maximiser la longueur.

---

## 🛠️ Astuces

- On **ne réécrit jamais** une somme déjà vue dans `sum_index_map` pour conserver l’index le plus ancien (ce qui garantit la plus grande longueur possible).
- Cet algorithme est optimal : **O(n)** en temps et **O(n)** en mémoire.
- Il fonctionne avec des nombres positifs, négatifs ou nuls.