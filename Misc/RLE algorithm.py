def run_length_encode(s):
    r = ""
    l = len(s)
    if l == 0:
        return ""
    if l == 1:
        return s + "1"
    last = s[0]
    cnt = 1
    i = 1
    while i < l:
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            r = r + s[i - 1] + str(cnt)
            cnt = 1
        i += 1
    r = r + s[i - 1] + str(cnt)
    return r

def run_length_decode(s):
    r = ""
    l = len(s)
    if l == 0:
        return ""
    if l == 1:
        return s
    i = 0
    while i < l:
        if s[i].isdigit():
            r = r + s[i - 1] * int(s[i])
        i += 1
    return r

print(run_length_encode("AAAABBBCCDAA"))
print(run_length_decode("A4B3C2D1A2"))
