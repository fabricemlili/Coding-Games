# Plus long sous-tableau avec une somme cible

### 🧩 Enoncé
Étant donné un tableau d'entiers `nums` et un entier `k`, écris une fonction qui retourne la longueur du plus long sous-tableau contigu dont la somme est égale à `k`.

### ✅ Exemples

```python
longest_subarray_sum([1, -1, 5, -2, 3], 3)  ➞ 4   # [1, -1, 5, -2]
longest_subarray_sum([-2, -1, 2, 1], 1)     ➞ 2   # [-1, 2]
longest_subarray_sum([1, 2, 3], 6)          ➞ 3   # [1, 2, 3]
longest_subarray_sum([1, 2, 3], 7)          ➞ 0   # aucun sous-tableau ne correspond
```

### 🎯 Objectif

1) Évaluer ta capacité à résoudre un problème algorithmique avec une solution efficace.

2) Implémenter une solution avec une complexité en temps linéaire O(n).

3) Utiliser des structures de données comme des dictionnaires (hashmaps) pour optimiser le calcul.

### 🧠 Astuce
1) Utilise une somme cumulative (`prefix sum`) que tu calcules au fur et à mesure.

2) À chaque itération, regarde si `somme_cumulative - k` a déjà été vue : cela veut dire qu’un sous-tableau avec la somme `k` existe entre l’index précédent et l’index actuel.

3) Garde en mémoire les premières occurrences des sommes cumulatives à l’aide d’un dictionnaire pour maximiser la longueur du sous-tableau.