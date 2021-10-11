A = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
B = [30, 40, 50, 60, 70, 80, 90, 100, 110]
key = 0
C = []
for i in range(0, len(A)):
    for j in range(key, len(A)):
        if B[i] < A[j]:
            C.append(B[i])
            break
        else:
            C.append(A[j])
    key = j
l = 2 * len(A) - len(C)
if l != 0:
    for i in range(len(A) - l, len(A)):
        C.append(A[i])
a = C[8]
b = C[9]
print(C)
print(len(C))
print((a + b) / 2)

