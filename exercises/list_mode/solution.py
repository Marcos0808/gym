from typing import Any

SUBMIT = True

def list_mode(_items: list[Any]) -> Any:
    """Returns the most frequent element in a list.

    Example usage:
    >>> list_mode([1, 2, 2, 3, 3, 3])
    3
    >>> list_mode(['a', 'b', 'a'])
    'a'
    """
    if not _items:
        return None
    control_1 = 0
    
    max_list = len(_items) - 1
    moda = list()
    while control_1 <= max_list:
        num = 0
        control_2 = 0
        index_1 = _items[control_1]
        while control_2 <= max_list:
            index_2 = _items[control_2]
            if index_1 == index_2:
                num = num + 1
            control_2 = control_2 + 1
        control_1 = control_1 + 1
        moda.append(num)
    max_num = max(moda)
    value = moda.index(max_num)
    result = _items[value]
    return result



def test() -> None:
    """Simple self-test for Most Common Element."""
    cases: list[tuple[list[Any], Any]] = [
        ([1, 2, 2, 3, 3, 3], 3),
        (["a", "b", "a"], "a"),
        ([10], 10),
    ]
    for items, expected in cases:
        try:
            res = list_mode(items)
            assert res == expected, (
                f"Failed for {items}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
