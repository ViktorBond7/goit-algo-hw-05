from timeit import timeit

def test_algorithm(algoritm, text, pattern):
    return timeit(lambda: algoritm(text, pattern), number=1)
