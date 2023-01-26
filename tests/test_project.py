"""Tests wether the project is even importable."""

try:
    import src
except:
    src = None


def test_import():
    assert src

