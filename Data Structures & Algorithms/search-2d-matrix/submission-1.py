class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        innerL, innerR = 0, len(matrix[0]) - 1

        while l <= r:
            arr = (r + l) // 2
            if target <= matrix[arr][innerR] and target >= matrix[arr][innerL]:
                return self.binarySearch(matrix[arr], target)
            elif target < matrix[arr][innerL]:
                r = arr - 1
            else:
                l = arr + 1
        return False

    def binarySearch(self, arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == arr[mid]:
                return True
            if target < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False