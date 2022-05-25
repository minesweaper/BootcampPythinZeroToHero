my_list = [1,2,3]
my_list2 = ['STRING', 100, 23.2]
print(len(my_list))
my_list3 = ['one', 'two', 'three']
print(my_list3[0])
print(my_list3[1:])
another_list = ['four', 'five']

new_list = my_list3 + another_list
new_list[0] = 'ONE ALL CAPS'
print(new_list)
new_list.append('six')
print(new_list)

new_list.pop()
print(new_list)
popped_item = new_list.pop()
print(popped_item)

new_list.pop(0)
print(new_list)

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,8,3]
# Sort does not return anything so a = list.sort() returns None
new_list.sort()
print(new_list)
num_list.sort()
print(num_list)

new_list.reverse()
num_list.reverse()
print(new_list)
print(num_list)
