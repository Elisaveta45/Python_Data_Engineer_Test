def gen_positive_number():
    n = 0
    while True:
        n += 1
        yield n


x = gen_positive_number()
for i in range(5):
    print(next(x))
