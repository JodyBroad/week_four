t1 = 'cat', 'dog', 'python', 'mouse', 'camel'
t2 = 'kelp', 'crab', 'lobster', 'fish'
for a, b, *c, d in t1, t2:
    print(a, b, c, d)
