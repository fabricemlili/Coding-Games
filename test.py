def longest_subarray_sum(nums: list[int], k: int) -> int:
    prefix_sum = 0
    seen_sums = {0: -1}  # To handle the case where subarray starts at index 0
    max_len = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        # Check if there is a previous prefix sum that would make the current sum - previous = k
        if (prefix_sum - k) in seen_sums:
            max_len = max(max_len, i - seen_sums[prefix_sum - k])

        # Only store the first occurrence of a prefix sum
        if prefix_sum not in seen_sums:
            seen_sums[prefix_sum] = i

    return max_len