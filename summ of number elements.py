a = 235

def summ(a):
    ans = 0
    if type(a) == int:
        if a < 0:
            ans = "'a' must be positive"
        else:
            for i in str(a):
                ans += int(i)

    else:
        ans = "it's not int"

    return ans

print(summ(a))