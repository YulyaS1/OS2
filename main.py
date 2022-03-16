import threading
import time
import hashlib
from itertools import product


def decrypt(hash_, num):
    h = hash_.encode()
    h = h.decode()
    for combos in product('abcdefghijklmnopqrstuvwxyz', repeat=5):
        if h == hashlib.sha256(''.join(combos).encode()).hexdigest():
            passwords[num] = ''.join(combos)


passwords = ['']*3
HASH = ['1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad',
        '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b',
        '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f']
thread_list = []
start = time.time()
print('\n<One thread>')
decrypt(HASH[0], 0)
decrypt(HASH[1], 1)
decrypt(HASH[2], 2)
end = time.time()
for i in range(3):
    print('Password {}:'.format(i+1), passwords[i])
print('Time taken: {}'.format(end-start))
print('\n<Multithreading>')
start = time.time()
for i in range(3):
    thr = threading.Thread(target=decrypt, name='thread{}'.format(i), args=(HASH[i], i))
    thr.start()
    thread_list.append(thr)
for i in thread_list:
    i.join()                # ждем завершения всех потоков
end = time.time()
for i in range(3):
    print('Password {}:'.format(i+1), passwords[i])
print('Time taken: {}'.format(end-start))
