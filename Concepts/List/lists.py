list = [1,2,3,4,5,6,7,8,6]
print(list)
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])
print(list[6])
print(list[7])
print(list[8])

#print elements
for x in list:
  print(x, end=" ")
  
# print indexes
print(f"\n{len(list)}")

n = len(list)
for length in range(n):
  print(length, list[length])
