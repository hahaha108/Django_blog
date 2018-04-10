# number = 0
# result = []
#
# for i in range(1,5,1):
#     for j in range(1, 5, 1):
#         for k in range(1, 5, 1):
#             if(i != j and j != k and i != k):
#                 result.append((i,j,k))
#
#
# number = len(result)
# print(number,result)

def shuixianhua(n):
    n = int(n)
    g = n % 10
    s = n //10 % 10
    b = n // 100
    if g**3 + s**3 + b**3 == n:
        return print(n)


if __name__ == '__main__':
    for i in range(100,999):
        shuixianhua(i)