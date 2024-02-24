from ctypes import c_int, CDLL
from time import perf_counter
import multiprocessing

# C-extension loading
lib = CDLL("E:\\Tim\\programming\\Python projects\\math-and-math-modelling\\.venv\\ht.dll")
# note: be careful with loading "ht.dll" - specify the correct path in your system


def htc(tk):
    return bool(lib.is_happy_ticket(c_int(tk)))  # improvement: accelerating processing with C


def ht(num):
    with multiprocessing.Pool() as pool:
        results = pool.map(htc, num)
    return results


if __name__ == "__main__":
    start = perf_counter()
    tickets = []
    tickets.extend(range(100000000))  # improvement: accelerated pool construction for multi-core processing

    results = ht(tickets)

    print(sum(results))  # improvement: no counter is used
    end = perf_counter()
    print(end - start)
