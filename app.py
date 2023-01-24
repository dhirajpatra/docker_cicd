"""
    This is a test script for CI/CD with Gitlab
"""


def test_method(num):
    """
    This method create a range of numbers and return the total

    Args:
        num (int): upto which you want to create the range

    Returns:
        int: it will return the total of range of number
    """
    tot = 0
    print("hello world")

    for i in range(num):
        print(f"testing for CI/CD {i}")
        tot += num
    return tot


if __name__ == "__main__":
    test_method(5)
