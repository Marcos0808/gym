SUBMIT = True


def palindrome(_text: str) -> bool:
    # noqa: ARG001
    """Checks if a string is a palindrome.

    Example usage:
    >>> palindrome("racecar")
    True
    >>> palindrome("hello")
    False
    """
    control = len(_text) - 1
    reverse = ""
    while control >= 0 :
        char = _text[control]
        reverse = reverse + char
        control = control - 1
        print(reverse)
    if reverse == _text:
        return True
    else :
        return False


def test() -> None:
    """Simple self-test for Palindrome."""
    cases = {"racecar": True, "hello": False, "aba": True}
    for text, expected in cases.items():
        try:
            res = palindrome(text)
            assert res == expected, (
                f"Failed for text='{text}': expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
