
"""
python program to Count the frequency of words appearing in a
string
Example: Enter the String: hi are you the one , this is you aren,t you this this this is
{'hi': 1, 'are': 1, 'you': 3, 'the': 1, 'one': 1, ',': 1, 'this': 4, 'is': 2, 'aren,t': 1}
Press any key to continue . . .

"""


def freq_words():
    str=input("Enter the String: ")
    #i need each word to be seprated using split() and retrun a list
    li= str.split()
    d={} # we need empty dict

    for i in li:
        if i not in d.keys():#if not already presesnt in dict start with 0, otherwise with 1 and increment as per loop
            d[i]=0 #dict initize with 0
        d[i]=d[i]+1
    print(d)

freq_words()


