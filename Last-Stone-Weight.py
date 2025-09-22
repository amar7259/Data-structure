# 2,3,6,4,2
# 6-4 = 2
# [2,3,2,2]

# 3-2 =1

# [1,2,2]

# 2-2 = 0

# Result = 1


# Logic?
# Brute force

# Time complexity --> 
# Space Complexity -->

# Sort max min 

# 64322
# 2322
# Sort again
# 3222
# 122
# sort again
# 221
# 01
# sort 
# 10

def soln(a):
    for idx in range(len((a))):
      print ("Loop time",idx)
    #   print(a)
      
      
      intrmd = sorted(a,reverse=True)
    #   print(intrmd)
      # intrmd1,intrmd2 =   intrmd[0:1],intrmd[1:2]
      rest = intrmd[2:]
    #   print("rest = ",rest)
      diff = intrmd[0] - intrmd[1]
    #   print("diff = ",diff)
      if diff != 0:

        rest.append(diff)
        print("here 1",rest)
        a = rest
        print("here 2",a)
        # print(rest)

        
        # soln(rest.append(diff))
        
    if len(rest) == 1:
          return rest[0]

answer = soln([2,3,6,4,2,7])

print(answer)




