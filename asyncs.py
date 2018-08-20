# def fib(n):
# 	# res = [1] * n
# 	# print(res)
# 	index = 0
# 	a = 0
# 	b = 1
# 	while index < n:
# 		yield b
# 		a, b = b, a + b
# 		index += 1
# print('-'*10 + 'test old fib' + '-'*10)
# for fib_res in fib(20):
# 	print(fib_res)
import random
import time


def stupid_fib(n):
	index = 0
	a = 0
	b = 1
	while index < n:
		sleep_cnt = yield b
		print('let me think {0} secs'.format(sleep_cnt))
		time.sleep(sleep_cnt)
		a, b = b, a + b
		index += 1
print('-'*10 + 'test yield send' + '-'*10)
N = 20
sfib = stupid_fib(N)
fib_res = next(sfib)
while True:
	print(fib_res)
	try:
		fib_res = sfib.send(random.uniform(0, 0.5))
	except StopIteration:
		break
