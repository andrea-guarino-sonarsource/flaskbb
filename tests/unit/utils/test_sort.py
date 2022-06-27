from flaskbb.cli.utils import quick_sort


def test_quick_sort():
    assert quick_sort([55, 42, 10]) == [10, 42, 55]
