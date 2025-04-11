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


print(longest_subarray_sum([1, -1, 5, -2, 3], 3))   # 4
print(longest_subarray_sum([-2, -1, 2, 1], 1))      # 2
print(longest_subarray_sum([1, 2, 3], 6))           # 3
print(longest_subarray_sum([1, 2, 3], 7))           # 0