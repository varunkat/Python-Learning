class Solution:
      def haha(self, nums):
          l = sorted(nums)
          na=[]
          for i in range(len(l)):
              if l[i] not in na:
                  na.append(l[i])
          k = len(na)
          print(na)
          return k

nums = [1,1,1,3,2,3,3,4]
x = Solution()
print(x.haha(nums))
