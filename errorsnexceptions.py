
# print("Temperatur converter")
# try:
#     # print(k)
#     c=int(input("Enter temperature in celcius:"))
#     f=c*9/4+32
#     print(f"Temp in fahrenheit is {f}")
# except:
#     print("Invalid input. Program terminated")

# print("-----------------------------------------")


# error exercise

# try:
#     n1=int(input("Enter first number:"))
#     n2=int(input("Enter second number:"))
#     x=n1/n2
#     print(f"Result is {X}")
# except ZeroDivisionError:
#     print("second number can't be zero")
# except ValueError:
#     print("Invalid input")
# except:
#     print("Some error occured")




# unpacking
# a,b = 10,2
# l=[1,2]
# try:
#     # print(a/0)
#     # print(a/b)
#     print(a/c)
#     # print(l[2])
#     print("9"+9)
# except (ZeroDivisionError, TypeError):
#     print("division error or invalid addition operations")
# except (ValueError,IndexError,NameError):
#     print("...")
# # except:
# #     print("some error occured")


# print()
# print()
# print("Code before try and catch")
# try:
#     z=10/2
#     temp = "23c"
#     print(int(temp))
# except NameError as e:
#     print("Name error occured:",e)
# except ValueError as ve:
#     print(ve)
# except Exception:
#     print("Some error occured")


# class Emp:
#     def __init__(self,name):
#         self.name=name

# e=Emp("Charan")
# e1="hi"
# print(e)
# print(isinstance(e1,Emp))
# print(type(e))


# try:
#     f=open("oops.py")
#     print(f.readlines()[400])
# except IndexError:
#     print("Some error occured")
# finally:
#     f.close()
#     print("Finally code will be executed always")


# nested try except

# try: 
#     l=[1,2,3]
#     print(l[0])
#     try:
#         k=1/0
#     except TypeError:
#         print("ZD error occured")

# except (IndexError,ZeroDivisionError):
#     print("Index/ZD error occured")





# Error occured in a function definition if not handled will be passed to function call

def func2():    
    print(f"Hello{j}")


def func1():
    try:
        # n=int(input("Enter a number:"))
        n=19
        print(f"Number entered is {n}")
        func2()
        
    except ValueError:
        print("Value error occured")

try:
    func1()
except ValueError:
    print("Name error occured")

# stack trace
"""
Traceback (most recent call last):
  File "c:\Users\Admin\OneDrive\Desktop\New folder\errorsnexceptions.py", line 118, in <module>
    func1()
    ~~~~~^^
  File "c:\Users\Admin\OneDrive\Desktop\New folder\errorsnexceptions.py", line 112, in func1    func2()
    ~~~~~^^
  File "c:\Users\Admin\OneDrive\Desktop\New folder\errorsnexceptions.py", line 104, in func2    print(f"Hello{j}")
                  ^
NameError: name 'j' is not defined
"""
