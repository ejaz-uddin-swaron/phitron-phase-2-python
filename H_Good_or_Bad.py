T = int(input())

while T != 0:
    S = input()
    if S.find("101") != -1 or S.find("010") != -1:
        print("Good")
    else:
        print("Bad")
    T -= 1