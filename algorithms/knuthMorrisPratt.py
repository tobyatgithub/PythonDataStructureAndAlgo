DEBUG = True


def buildPartialMatchTable(pattern_string):
    i, j = 1, 0
    N = len(pattern_string)
    res = [0 for _ in range(N)]

    while i < N:
        if pattern_string[i] == pattern_string[j]:
            j += 1
            res[i] = j
            i += 1
        else:
            if j > 0:
                j = res[j - 1]
            else:
                res[i] = 0
                i += 1
    return res


# test buildPartialMatchTable
print(buildPartialMatchTable("xyztruxyzo"))
print("==" * 20)
print(buildPartialMatchTable("ababcaabc"))


def KMPSearch(pattern, text):
    N = len(text)
    M = len(pattern)

    lsp = buildPartialMatchTable(pattern)

    i, j = 0, 0
    while i < N:
        if pattern[j] == text[i]:
            if DEBUG:
                print(
                    f"i = {i}, j = {j}, pattern match between pattern[j] = {pattern[j]} and text[i] = {text[i]}."
                )
            i += 1
            j += 1
        if j == M:
            print(f"i = {i}, j = {j}, Found pattern at index ", i - j)
            return i - j
        elif i < N and pattern[j] != text[i]:
            if DEBUG:
                print(
                    f"i = {i}, j = {j}, pattern NOT match between p[j] and t[i]."
                )
            if j != 0:
                if DEBUG:
                    print(f"j != 0, thus j updated from {j} to {lsp[j-1]}")
                j = lsp[j - 1]
            else:
                if DEBUG:
                    print(f"j == 0, then we change i from {i} to {i+1}")
                i += 1
    return -1


txt = "ababcaababcaabc"
pat = "ababcaabc"
KMPSearch(pat, txt)
print([(i, txt[i]) for i in range(len(txt))])
