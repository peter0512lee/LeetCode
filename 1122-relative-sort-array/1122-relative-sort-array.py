class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sorted_lst = []

        for x in arr2:
            while x in arr1:
                sorted_lst.append(x)
                arr1.remove(x)

        return(sorted_lst + sorted(arr1))