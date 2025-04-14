def longest_subarray_sum(nums: list[int], k: int) -> int:
    sum_index_map = {}  # Dictionnaire pour stocker la première occurrence de chaque somme cumulative
    cumulative_sum = 0
    max_length = 0

    for i, num in enumerate(nums):
        cumulative_sum += num  # On met à jour la somme cumulative jusqu'à l'index i

        # 🟢 Cas 1 : La somme cumulative elle-même est égale à k
        if cumulative_sum == k:
            max_length = i + 1

        # 🟢 Cas 2 : (somme cumulative - k) a déjà été vue
        # Cela signifie qu'il y a un sous-tableau de somme k entre cette ancienne position et l'index i
        if (cumulative_sum - k) in sum_index_map:
            length = i - sum_index_map[cumulative_sum - k]
            max_length = max(max_length, length)

        # 🟢 Cas 3 : Enregistrer la première apparition de la somme cumulative
        # On ne l'écrase pas si elle existe déjà, pour garder le sous-tableau le plus long
        if cumulative_sum not in sum_index_map:
            sum_index_map[cumulative_sum] = i

    return max_length
















def run_tests():
    test_cases = [
        (([1, -1, 5, -2, 3], 3), 4),
        (([-2, -1, 2, 1], 1), 2),
        (([1, 2, 3], 6), 3),
        (([1, 2, 3], 7), 0),
        (([1, -1, 1, -1, 1], 1), 5),  # Alternance, somme intermittente
        (([0, 0, 0, 0], 0), 4),       # Tous nuls
        (([3, 1, -1, 2, -2, 4], 5), 4), # Plusieurs possibilités
        (([], 0), 0),                # Cas vide
        (([5], 5), 1),               # Cas minimal
        (([5], 3), 0),               # Cas minimal sans correspondance
    ]

    for i, ((nums, k), expected) in enumerate(test_cases, 1):
        try:
            result = longest_subarray_sum(nums, k)
            assert result == expected, f"Test {i} échoué : attendu {expected}, obtenu {result}"
            print(f"✅ Test {i} OK")
        except AssertionError as e:
            print("❌", e)
        except Exception as e:
            print(f"⚠️ Erreur inattendue dans le test {i} :", e)

run_tests()
