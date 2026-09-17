class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last_occurence = {}
        
        for i,char in enumerate(s):
            last_occurence[char] = i

        result = []
        start = 0
        end = 0

        for i,char in enumerate(s):

            end = max(end,last_occurence[char])

            if i==end:

                partition_size = i-start+1
                result.append(partition_size)
                start = i+1

        return result