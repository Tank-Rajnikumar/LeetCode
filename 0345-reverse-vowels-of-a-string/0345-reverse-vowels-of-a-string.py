class Solution:
    def reverseVowels(self, s: str) -> str:
        lst=[]
        sl=[]
        for i in range(len(s)):
            if s[i] in ['A',"E","I","O","U","a","e","i","o","u"]:
                lst.append(i)
                sl.append(s[i])
        sl=sl[::-1]
        print(lst)
        print(sl)
        j=0
        for i in lst:
            s=s[:i]+sl[j]+s[i+1:]
            j+=1
        return s