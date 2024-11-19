from numlib.converters import opposit


def test_opposit() -> None:
    assert 1 == opposit(-1)
    assert -1 == opposit(1)
    assert 0 == opposit(0)
    assert -2.3 == opposit(2.3)