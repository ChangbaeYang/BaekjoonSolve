import sys
input = sys.stdin.readline

N = int(input())
nums = set(map(int, input().split()))
nums = list(nums)
nums.sort()

for i in range(len(nums) - 1):
    print(nums[i], end = ' ')
print(nums[-1])
