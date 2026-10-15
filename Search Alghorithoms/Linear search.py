lst = [42, 17, 89, 3, 55, 22, 17, 91, 64, 5, 89, 12]
seen = []
val = 0
idx = 0

for i in range(len(lst)):
  if lst[i] in seen:
    val = lst[i]
    idx = i
    break
  seen.append(lst[i])

print("The duplicate is", val)
print("The index is", idx)