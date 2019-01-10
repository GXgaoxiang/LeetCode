def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    left = 0
    right = len(height) - 1
    max_v = 0
    while left < right:
        if height[left] > height[right]:
            max_v = max(max_v, (right - left) * min(height[left], height[right]))
            right -= 1
        else:
            max_v = max(max_v, (right - left) * min(height[left], height[right]))
            left += 1
    return max_v