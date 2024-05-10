class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        left, right = 0, 1
        frac_dict = {}

        while right < len(arr):
            frac = arr[left] / arr[right]
            frac_dict[frac] = (arr[left], arr[right])
            right += 1
            if right == len(arr):
                right = left + 1
                left += 1

        # sort the fractions by their value
        sorted_fracs = sorted(frac_dict.items(), key=lambda x: x[0])

        # get the kth smallest fraction
        kth_smallest = sorted_fracs[k-1][0]

        return [frac_dict[kth_smallest][0], frac_dict[kth_smallest][1]]