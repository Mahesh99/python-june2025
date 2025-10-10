import time
import threading

# def print_cube(num):
#     print("starting print cube")
#     time.sleep(3)
#     print(f"Cube: {(num * num * num)}")

# print_cube(10)

"""
g=10

def myfunc(name):
    print(f"thread {name} starting {g}")
    time.sleep(3)
    print(f"thread {name} ending")

# myfunc(1)
# myfunc(2)
# myfunc(3)
# myfunc(4)
# myfunc(5)

t1=threading.Thread(target=myfunc,args=(1,))
t1.start()
t2=threading.Thread(target=myfunc,args=(2,))
t2.start()
t3=threading.Thread(target=myfunc,args=(3,))
t3.start()
t4=threading.Thread(target=myfunc,args=(4,))
t4.start()
t5=threading.Thread(target=myfunc,args=(5,))
t5.start()
print("Hi this is a main thread")
"""

# we can't use threads everytime
# we can only use them in i/o bound tasks
# we can't use them in cpu bound tasks

# 1.multiprocessing-heavy
# each process has its own memory
# 2.multi threading-light
# multiple threads share the same memory

# using multiprocessing is preferred when you have cpu intense tasks
# using threads is preferred for i/o intense operations
#input devices: keyboard, mouse, scanner
#output devices: monitor, printer


"""
def print_nums(n):
    for i in range(1,n+1):
        print(i)
        time.sleep(1)


t=threading.Thread(target=print_nums,args=(5,))
t.start()
t2=threading.Thread(target=print_nums,args=(10,))
t2.start()
t.join()
t2.join()
print("This is main thread")
"""
# race condition
counter=0
lock=threading.Lock()

def increment():
    global counter
    print("increment")
    for _ in range(1000):
        lock.acquire()
        counter+=1
        lock.release()

# def decrement():
#     print("decrement")
#     global counter
#     for _ in range(1000):
#         counter-=1

# increment()
# print(counter)
t=threading.Thread(target=increment)
t.start()
t2=threading.Thread(target=increment)
t2.start()
t.join()
t2.join()
print(counter)
