from typing import List

def max_treasure(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    n, m = len(grid), len(grid[0])
    dp = [row[:] for row in grid]  # copie de la grille

    for i in range(1, n):
        for j in range(m):
            max_prev = dp[i-1][j]  # au-dessus
            if j > 0:
                max_prev = max(max_prev, dp[i-1][j-1])  # en haut à gauche
            if j < m - 1:
                max_prev = max(max_prev, dp[i-1][j+1])  # en haut à droite
            dp[i][j] += max_prev

    return max(dp[-1])



















def run_tests():
    test_cases = [
        # Test 1 : Exemple classique
        {
            "input": [
                [1, 3, 1, 5],
                [2, 2, 4, 1],
                [5, 0, 2, 3],
                [0, 6, 1, 2]
            ],
            "expected": 17
        },
        # Test 2 : Grille avec une seule ligne
        {
            "input": [[10, 20, 30]],
            "expected": 30
        },
        # Test 3 : Grille avec une seule colonne
        {
            "input": [
                [1],
                [2],
                [3],
                [4]
            ],
            "expected": 10
        },
        # Test 4 : Grille avec toutes les valeurs à zéro
        {
            "input": [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ],
            "expected": 0
        },
        # Test 5 : Grille vide
        {
            "input": [],
            "expected": 0
        }
    ]

    for i, test in enumerate(test_cases):
        try:
            result = max_treasure(test["input"])
            assert result == test["expected"], f"❌ Test {i + 1} échoué: attendu {test['expected']}, obtenu {result}"
            print(f"✅ Test {i + 1} réussi")
        except Exception as e:
            print(f"⚠️ Erreur inattendue dans le test {i + 1} :", e)

# Lancer les tests
run_tests()
