import time

def cond(x: int) -> bool:
    for i in range(2, 21):
        if x % i != 0:
            return False
    return True

res = 1
stop = cond(res)

start = time.time()
while not stop:
    res = res + 1
    stop = cond(res)

end = time.time()
running = end - start

print(res, running)