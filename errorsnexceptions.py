
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
print("Code before try and catch")
try:
    z=10/2
    temp = "23c"
    print(int(temp))
except NameError as e:
    print("Name error occured:",e)
except ValueError as ve:
    print(ve)
except Exception:
    print("Some error occured")


# class Emp:
#     def __init__(self,name):
#         self.name=name

# e=Emp("Charan")
# e1="hi"
# print(e.name)
# print(isinstance(e1,Emp))
# print(type(e))
