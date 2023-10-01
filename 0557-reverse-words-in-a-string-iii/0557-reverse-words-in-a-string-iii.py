class Solution:
    def reverseWords(self, s: str) -> str:
        slist=s.split()
        st=[]
        if len(slist)<1:
            return None
        for i in slist:
            st.append(i[::-1])
        if len(st)<1:
            return None
        a=" ".join(st)
        return a