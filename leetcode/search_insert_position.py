def search_insert(nums, target):
        low, high = 0, len(nums)-1
        mid = int((high + low)/2)

        while low <= high:
            mid = int((high + low)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1

        if target > nums[mid]:
            return mid + 1
        else:
            return mid
