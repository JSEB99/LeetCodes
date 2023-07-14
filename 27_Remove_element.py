class Remove:
    def removeElement(self,nums: list[int],val: int)->int:
        '''
        Remove all concurrences from a integer given list
        '''
        while val in nums:
            nums.remove(val)
        k = len(nums)

        return k 

lista = Remove()
print(lista.removeElement([3,2,2,3],3))
