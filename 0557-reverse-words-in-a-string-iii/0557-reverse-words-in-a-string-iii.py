class Solution:
    def reverseWords(self, s: str) -> str:
        slist=s.split()
        st=[]
        for i in slist:
            st.append(i[::-1])
        a=" ".join(st)
        return a