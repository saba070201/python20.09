# # less4
# import colorama 
# print(colorama.Fore.YELLOW)
# print('this is yellow !!!')
# def bad_print(word):
#   print(word)
# def good_print(*args):
#   print(args[0])
# # bad_print('misha','python')
# good_print('misha','python','=love')
# def calculator(a,b,operation='+'):
#   if operation=='+':
#     c=a+b
#     print(c)
#   elif operation=='-':
#     c=a-b
#     print(c)
# calculator(3,2)
# print('a','b')
path='less4/files/text.txt'
file=open(path,'w')
file.write('hello world!')
file.close()