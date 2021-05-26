def my_gen():
    yield 'あいうえお'
    yield 'かきくけこ'
    yield 'さしすせそ'

for value in my_gen():
    print(value)

gen = my_gen()
print(gen)
for value in gen:
    print(value)

