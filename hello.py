string=input("Enter your string: ")
if(string == string[:: -1]):
    print("Palindrome string")
else:
    print("Not Palindrome String")





# def decor1(func):
#     def inner_func():
#         x=func()
#         return x * x
#     return inner_func
# def decor2(func):
#     def inner_func():
#         x=func()
#         return 2 * x
#     return inner_func
# @decor1
# @decor2
# def num():
#     return 10
# print(num()) #decor1(decor2(num))

