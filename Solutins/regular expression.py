class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s==""  :
            if p == "" : return True
            if  len(p)>1 and p[1]=='*':
                return self.isMatch( s, p[2:])  # end of s  and last char in p is '*'
            return False
        if p=="" : return False
        if s[0]==p[0] or p[0]=='.':
            if len(p)>1 and p[1]=='*':  #if next char in p is '*'
                if  self.isMatch(s[1:], p) == False:
                    return self.isMatch(s[0:], p[2:])  # repeat case is failed, then skip '*'
                else: return True
            else:  return self.isMatch(s[1:],p[1:])
        if  len(p)>1 and p[1]=='*':   # if next char in p is '*' means repeat 0 times
            return self.isMatch(s, p[2:])  # so, skip '*'
        return False
obj1=Solution()
y=obj1.isMatch("aa","a*")
print(y)