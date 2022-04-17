from typing import List


class Solution:
	def checkPermutation(self,s1, s2):

		lists = []
		for i in range(len(s2) + 1):
			for j in range(i):
				lists.append(s2[j: i])	 		

		print(lists)




if __name__ == '__main__':

  s1='ab'
  s2='eidboaoo'

  t = Solution()
  print(t.checkPermutation(s1, s2))