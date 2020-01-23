import random
# arr = ["Artem","Valentin","Stepan","Viktor"]

# arr2 = ["Olga","Olesia","Alina","Anna"]
# arr2.extend(arr)
# arr3 = arr2[::3]
# # print(arr2,arr3)
# arr2.reverse()

# # file = open("list.txt",'w')
# # file.write(str(arr2))
# # file.close()
# # for item in arr2:
# #     print(item)
# arr3.append("Steve")
# print(arr3)
arr = []

for a in range(0,21):
    arr.append(random.randint(0,99))
    
arr.sort()
min_value = min(arr)
max_value = max(arr)
min_index = arr.index(min_value)
max_index = arr.index(max_value)
z = arr[max_index]
arr[max_index] = arr[min_index]
arr[min_index] = z

print("summ_element indexes//2=1: ",sum(arr[1::2]))
arr2 = []
arr2.extend(arr)
print("Array was copied: ",arr2)
arr3 = arr2 + arr
print("3rd array is: ",arr3)

