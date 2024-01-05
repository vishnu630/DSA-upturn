class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap={}
        for n in nums:
            hashmap[n]=hashmap.get(n,0)+1
        sorted_hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)[:k]
        top_k_frequent = [key for key, _ in sorted_hashmap[:k]]
        return top_k_frequent


        