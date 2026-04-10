class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_to_elements = {i:[] for i in range(1, len(nums)+1)}
        which_bucket = {}
        for num in nums:
            which_bucket[num] = which_bucket.get(num, 0) + 1
        for num, frequency in which_bucket.items():
            count_to_elements[frequency].append(num)
        k_most_frequent = []
        for i in range(len(nums), 0, -1):
            for num in count_to_elements[i]:
                k_most_frequent.append(num)
                if len(k_most_frequent) == k:
                    return k_most_frequent


        