# # Map is function used to convert elements from string to integer, etc.
# a = input().split()
# numbers = (10,20,30,40,50)
# # a = list(map(int,input().split()))
# # # print(a)
# def addition(n):
#     return n+n
# numbers = (1,2,3,4)
# result = map(addition, numbers)
# print(list(result))
# #We can also use lambda function with map to achieve above results.
# numbers1=(1,2,3)
# # numbers2=(4,5,6)
# result= map(lambda x: x + x, numbers1)
# print(list(result))
# a = input().split()
numbers = ("10,20,30,40,50")
l1 = numbers.split()
# # print(type(numbers[0]))
# n = list(map(int, numbers.split()))
# print(n)
l1 = list(map(int,numbers.split()))
print(l1)
