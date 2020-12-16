"""
Quick select general template, to find k-th smallest item in an array
"""


def quickSelect(self, start, end, nums_array, k):
        '''
        start: start index of the num_array
        end:  end index of the num_array
        num_array: An array to find the kth smallest item
        k:  the number of kth
        usage: quickSelect(0, len(nums_array) - 1, nums_array, k)
        '''
        if start == end:
            return nums_array[start]
        
        left, right = start, end
        pivot = nums_array[(start + end) // 2]
        
        while left <= right:
            while left <= right and nums_array[left] < pivot:
                left += 1
            while left <= right and nums_array[right] > pivot:
                right -= 1
            if left <= right:
                nums_array[left], nums_array[right] = nums_array[right], nums_array[left]
                left += 1
                right -= 1
        
        if start + k - 1 <= right:
            return self.quickSelect(start, right, nums_array, k)
        elif start + k - 1 >= left:
            return self.quickSelect(left, end, nums_array, k - (left - start))
        else:
            return nums_array[left - 1]