class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freqs = [0]*26

        for i in tasks:
            freqs[ord(i)-ord('A')]+=1

        max_freq = max(freqs)

        num_max_freq = freqs.count(max_freq)

        solution = ((n+1) * (max_freq-1))+num_max_freq

        return max(len(tasks),solution)