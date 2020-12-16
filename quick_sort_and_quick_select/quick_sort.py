"""
Quick sort general template ascending
"""

def quickSort(self, start, end, num_array):
        '''
        start: start index of the num_array
        end:  end index of the num_array
        num_array: An array to be sorted
        usage: quickSort(0, len(nums_array) - 1, nums_array)
        '''
        if start >= end:
            return num_array
        
        left, right = start, end
        # key point 1: pivot is the value,  not the index
        pivot = num_array[(start + end) // 2]
        
        # key point 2: every time you compare left & right, it should be
        # left <= right not left < right
        while left <= right:
            while left <= right and num_array[left] < pivot:
                left += 1
            while left <= right and num_array[right] > pivot:
                right -= 1
            if left <= right:
                num_array[left], num_array[right] = num_array[right], num_array[left]
                left += 1
                right -= 1
        
        self.quickSort(start, right, num_array)
        self.quickSort(left, end, num_array)
        return num_array