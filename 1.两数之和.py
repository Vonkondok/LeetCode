# python3
class Solution():
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])
                           
        sumlist = []
        i=0; j=len(nums)-1
        
        if nums[sorted_id[i]] + nums[sorted_id[j]] == target:
            sumlist = [sorted_id[i],sorted_id[j]]
        
        else:
            while nums[sorted_id[i]] + nums[sorted_id[j]] != target:
                if nums[sorted_id[i]] + nums[sorted_id[j]] > target:
                    j -= 1
                elif nums[sorted_id[i]] + nums[sorted_id[j]] < target:
                    i += 1
                    
                sumlist = [sorted_id[i],sorted_id[j]]
                
        return sumlist
