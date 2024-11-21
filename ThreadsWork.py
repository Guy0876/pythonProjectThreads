import random
import threading
import time


def func1():
    name = threading.current_thread().name
    for i in range(99):
        if (i + 1) % 2 == 0:
            print(i, name)


def func2():
    name = threading.current_thread().name
    for i in range(99):
        if (i + 1) % 2 == 1:
            print(i, name)


print("Main : before creating thread")

x1 = threading.Thread(target=func1, name = 'x1')
x2 = threading.Thread(target=func2, name = 'x2')

print("Main : before running thread")

x2.start()
x1.start()

print("Main : wait for the thread to finish")

x1.join()
x2.join()

print("Main : finish!")

def isPrime(min, max):
    for i in range(min, max):
        if checkIsPrime(i):
            print(i)

def checkIsPrime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True

x3 = threading.Thread(target=isPrime, args=(1, 1000))

x3.start()
x3.join()

threads = []
i = int(input("enter a number"))
j = 0
while i - 1000 > 0:
    thread = threading.Thread(target=isPrime(j + 1, j + 1000))
    threads.append(thread)
    thread.start()
    j += 1000
    i -= 1000
thread = threading.Thread(target=isPrime(j, j + i))
threads.append(thread)
thread.start()
for thread in threads:
    thread.join()

N = 10
distances = [0] * N

def simulate_runner(index):
    covered_distance = 0
    while True:
        distances[index] += 10
        time.sleep(random.randint(1, 5))

threads = []
for i in range(N):
    thread = threading.Thread(target=simulate_runner, args=(i,))
    threads.append(thread)
    thread.start()
time.sleep(20)
distances_copy = distances[:]
max_distance = max(distances_copy)
winner_index = distances_copy.index(max_distance)
print(f"The runner with index {winner_index} covered the largest distance: {max_distance} meters.")