SUBMIT = True


def fibonacci(n: int) -> int:
    """Calculates the n-th Fibonacci number.

    Example usage:
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(10)
    55
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    num_1 = 0
    num_2 = 1
    var = 2
    while var <= n:
        num = num_1 + num_2
        num_1 = num - num_1 
        num_2 = num
        var = var + 1
    return num      
        

def test() -> None:
    """Simple self-test for Fibonacci."""
    cases = {0: 0, 1: 1, 5: 5, 10: 55}
    for n, expected in cases.items():
        try:
            res = fibonacci(n)
            assert res == expected, f"Failed for n={n}: expected {expected}, got {res}"
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
