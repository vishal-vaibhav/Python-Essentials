
#program to findout common letters between two strings
# 1)NAINA > NAI
# 2)REENE > REN
# common in both is N

def common_letters():
    str1 = input("Enter the first String: ")
    str2 = input("Enter the Second String: ")
    #set() to filter duplicate
    s1=set(str1)
    s2=set(str2)

    #check if code is working
    print(s1)
    print(s2)

    # use & operator to filter only common letters from both string
    cl = s1 & s2
    print("common letters are: ")
    print(cl)

common_letters()