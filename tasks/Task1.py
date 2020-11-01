from array import *
2    lst = array('i',[4,5,7,5,4,8])
3    
4    ndupl = set() # create empty set
5    
6    # loop trough the elements inside the list
7    for i in lst:
8        if lst.count(i) == 1:
9            ndupl.add(i)
10           result=sum(ndupl)
11   
12   # show final data
13   print(result)
