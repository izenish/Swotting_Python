# HackerRank Question
# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# from time import perf_counter
n = 5
x = 'asscsc'
count = 0
infine = x*(n+1)
print(f"this is the actual string {infine}")
toStringg = [separated for separated in infine]
print(toStringg)
for x, y in enumerate(toStringg):
    if(x < n and y == "a"):
        count = count+1
print(count)
print("__________________________________")
# s = perf_counter()
# for z in range(1000000000000):
#     print(z, end="\r")
# end = perf_counter()
# print(f'Time elapsed is :{end-s}')
# # isd = ["K", 'a', 'j', 'o', 'l']
# print(infine)
# for x, y in enumerate(isd):
#     print(f"X is {x} and Count is {y}")
# # limit = [z for z, y in enumerate(infine) if y <= n]
# # print(limit)
# for(i=0;i<10;i++)
print("__________________________________")
# n = 1000000000000

# s = 'a'
# count = 0
# infine = x*(n+1)
# alpha = ''
# r = 0
# l = len(s)
# for i in range(0, l):
#     if s[i] == 'a':
#         r += 1
# r *= int(n / l)
# for i in range(0, n % l):
#     if s[i] == 'a':
#         r += 1

# print(r, end="\r")
# print(f"this is the actual string {infine}")
# # print(infine[1])
# # toStringg = [separated for separated in infine]
# for x in range(n):
#     alpha = alpha+infine[x]

# print(alpha)
# print(alpha.count('a'))


# n=5
n = 549382313570

s = "epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq"
count1 = 0
countA = 0
totalA = 0
quotient = int(n/len(s))  # gives quotient that is completed odd strings
count1 = quotient*(s.count('a'))

remainder = int(n % len(s))
remainingOddStr = s[:remainder]  # remaining odd str

totalA = count1+remainingOddStr.count('a')
print(int(totalA))
#  https://youtu.be/XWG58qrcB50
