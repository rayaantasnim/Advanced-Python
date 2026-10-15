lst = [2, 5, 5, 5, 8, 12, 15, 15, 20]
target = int(input("Enter the number please: "))

low = 0
high = len(lst) - 1
idx = -1

while (low <= high):
  mid = (low + high) // 2

  if (lst[mid] == target):
    idx = mid
    break
  
  elif (lst[mid] < target):
    low = mid + 1
    
  else:
    high = mid - 1

if (idx == -1):
  print("The number is not found")

else:
  positions = []
  i = idx
  while (i >= 0 and lst[i] == target):
    positions.append(i)
    i -= 1
  positions.sort()

  i = idx + 1
  while (i < len(lst) and lst[i] == target):
    positions.append(i)
    i += 1

  print("The positions are", positions)