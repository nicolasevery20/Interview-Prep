class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        smallerThan=0
        targetCount=0
        idx=[]
        for i in nums:
            if i == target:
                targetCount+=1
            if i<target:
                smallerThan+=1
        for i in range(targetCount):
            idx.append(smallerThan+i)
        return idx
