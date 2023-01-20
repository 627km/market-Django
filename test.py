def test(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

test(10, 20, 30, 40, 50, pk=123, abs=234)