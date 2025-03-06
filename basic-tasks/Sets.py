x = set()  #Creates a set (using constructor; otherwise creates a dictionary)
#s = {} # Creates a disctionary
s = {4,32,2,2} # set literal + set removes duplicate value
s2 = [4,32,1,5]

print(2 in s2)
print(4 in s)   #Looks if 4 is in s or not
# NOTE line 7 will perform much much much much much faster thank line 6

# Set is very beneficial when it comes to lookling things up, checking if something is in there, removing and deleting

print(s.union(s2))
print(s.difference(s2))
print(s.intersection(s2))
print(s.symmetric_difference(s2))