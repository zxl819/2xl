s = "MCMXCIV"
#print(s.index('L'))
print(s[1])
print(len(s))
def romanToInt(s):
    ans =0
    i = 0
    #X_ind = s.index('X')
    #C_ind = s.index('C')
    while i < len(s):
        if s[i] == 'I':
            if s[i+1] == 'V':
                ans += 4
                i += 2
            elif s[i+1] == 'X':
                ans += 9
                i += 2
            else:
                ans += 1
                i += 1

        elif s[i] == 'X':
            if s[i+1] == 'L':
                ans += 40
                i += 2
            elif s[i+1] == 'C':
                ans += 90
                i += 2
            else:
                ans += 10
                i += 1

        elif s[i] == 'C':
            if s[i+1] == 'D':
                ans += 400
                i += 2
            elif s[i+1] == 'M':
                ans += 900
                i += 2
            else:
                ans += 100
                i += 1

        elif s[i] == 'V':
            ans += 5
            i += 1

        elif s[i] == 'L':
            ans += 50
            i += 1

        elif s[i] == 'D':
            ans += 500
            i += 1

        elif s[i] == 'M':
            ans += 1000
            i += 1
    return ans

print(romanToInt(s))

def romanToInt2(s):
    d ={'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
    return sum(d.get(s[max(i-1,0):i+1],d[n]) for i,n in enumerate(s))
print(romanToInt2(s))





