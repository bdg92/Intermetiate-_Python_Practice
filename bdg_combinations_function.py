## Let's try making a function called bdg_combination which will take argument as a list and length of bdg_combination
## And will return the possible combinations of the elements of the list.

def bdg_combination (l,g):
    n = len(l)
    nl = []
    el = []
    loop = 0
    while loop < n-1:
        for x in range(1,n):
            if loop ==x or x< loop:
                continue
            el = (l[loop],l[x])
            nl.append(el)
        loop +=1
    print(nl)
    print("No. of combinations which can be made from this set of data is:",len(nl))

l = [1,2,3,4,5,6]
g =2
bdg_combination(l,g)