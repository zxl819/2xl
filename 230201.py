key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"


def decodeMessage(key,message):
    cur = 'a'
    rules = dict()

    for c in key:
        if c != ' ' and c not in rules:
            rules[c] = cur
            cur = chr(ord(cur)+1)

    ans = " ".join(rules.get(c," ") for c in message)
    return ans

print(decodeMessage(key,message))

