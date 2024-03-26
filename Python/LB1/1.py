import timeit

def remove(some_list, x):
    isFound = False
    tmp_list = []
    for elem in some_list:
        if elem != x or (elem == x and isFound):
            tmp_list.append(elem)
        else:
            isFound = True
    some_list.clear()
    some_list.extend(tmp_list)
    return


def reverse(some_list):
    tmp_list = some_list[::-1]
    some_list.clear()
    some_list.extend(tmp_list)


def keys(some_dict):
    tmp_keys = []
    for key, value in some_dict.items():
        tmp_keys.append(key)
    return tmp_keys

print("Own realisation")

test_d = {'a': 1, 'b': [1], 'c': 100}
test_list = [i for i in range(320)]
test_list_2 = [i for i in range(40000)]

time_remove = timeit.timeit(lambda: remove(test_list, 500), number=10000)
print("remove:", time_remove)

time_reverse = timeit.timeit(lambda: reverse(test_list_2), number=10000)
print("reverse:", time_reverse)

time_keys = timeit.timeit(lambda: keys(test_d), number=1200000)
print("keys:", time_keys)

print("Python realisation")

test_d = {'a': 1, 'b': [1], 'c': 100}
test_list = [i for i in range(320)]
test_list_2 = [i for i in range(40000)]
time_remove = timeit.timeit(lambda: [x for x in test_list if x != 500], number=10000)

print("remove:", time_remove)

time_reverse = timeit.timeit(lambda: test_list_2.reverse(), number=10000)
print("reverse:", time_reverse)

time_keys = timeit.timeit(lambda: test_d.keys(), number=1200000)
print("keys:", time_keys)

print('\nTests\n')


print('remove 5')
test_list = [1, 2, 3, 4, 5, 5]
print(test_list, end = "=>")
remove(test_list, 5)
print(test_list)

print('reverse list')
test_list = [1, 2, 3, 4, 5]
print(test_list, end = "=>")
reverse(test_list)
print(test_list)

print('dict keys')
test_dict = {'a': 1, 'b': 2, 'c': 3}
print(test_dict, end = ", keys=")
print(keys(test_dict))
