import argparse
import timeit

parser = argparse.ArgumentParser(
    description='Test convert iterator to list')
parser.add_argument(
    '--size', help='The number of elements from iterator')

args = parser.parse_args()

size = int(args.size)
repeat_number = 10000

# do not wait too much if the size is too big
if size > 10000:
    repeat_number = 100


def test_convert_by_type_constructor():
    list(iter(range(size)))


def test_convert_by_list_comprehension():
    [e for e in iter(range(size))]


def test_convert_by_unpacking():
    [*iter(range(size))]


def get_avg_time_in_ms(func):
    avg_time = timeit.timeit(func, number=repeat_number) * 1000 / repeat_number
    return round(avg_time, 6)


funcs = [test_convert_by_type_constructor,
         test_convert_by_unpacking, test_convert_by_list_comprehension]

print(*map(get_avg_time_in_ms, funcs))
