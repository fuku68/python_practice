import math

# 素数を求めるジェネレーター
def get_primes():
    num = 2 # 素数の開始値
    # 2から順に素数判定し、素数の場合にだけyield（無限ループ）
    while True:
        if is_prime(num):
            yield num
        num += 1

# 引数valueが素数かどうかを判定
def is_prime(value):
    result = True # 素数かどうかを表すフラグ
    # 2 ～ sqrt(value)で、valueを割り切れる（＝余りが0）ものがあるか
    for i in range(2, math.floor(math.sqrt(value)) + 1): 
        if value % i == 0:
            result = False # 割り切れるものがあれば素数でない
            break
    return result

gen = get_primes()
for prime in gen:
    print(prime)
    if prime > 100:
        gen.close()

gen = get_primes()
for prime in gen:
    print(prime)
    if prime > 100:
        gen.throw(ValueError('result is over 100!'))
