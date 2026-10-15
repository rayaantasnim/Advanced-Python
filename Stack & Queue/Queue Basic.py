#Queue Deta Stracture -> Horizontal deta set
queue = []

#enqueue -> Add at the last point
queue.append(20)
queue.append(896)
queue.append(3254)
queue.append(54)
queue.append(7689)
queue.append(3245)
queue.append(543)
queue.append(454375)
queue.append(45657)
queue.append(34526)


#dequeue -> Remove the first index
queue.pop(0) 

#Front/peek -> Showcase the first element
print(queue[0])

#isEmpty
if (queue):
    print("Not empty!")

else:
    print("Empty")