# input: [19,22,3,28,26,17,18,4,28,0]
# output: [0,28,4,18,17,26,28,3,22,12]

def rev_array(lst):
  rev=[]
  for i in range(len(lst)-1,-1,-1):
    rev.append(lst[i])
  
  return rev

arr=[19,22,3,28,26,17,18,4,28,0]
print("input:",arr)
print("output:",rev_array(arr))