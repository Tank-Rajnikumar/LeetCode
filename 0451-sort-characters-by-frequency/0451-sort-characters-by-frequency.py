from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        dicS=Counter(s)
        ans=dict(sorted(dicS.items(),key=lambda x:x[1],reverse=True))
        print(ans)
        AnsStr=''
        for i in ans.keys():
            for j in range(ans[i]):
                AnsStr+=i
        print(AnsStr)
        return AnsStr