import pytest
from geometry import Square, Circle, area_stats
def test_square_area_zero_and_positive():
    # Arrange: choose side lengths
    s0 = Square(0)
    s2 = Square(2)
    # Act: compute areas
    # Assert: use pytest.approx to compare with expected
    assert s0.area() == 0
    assert s2.area() == pytest.approx(4.0)

def test_stats_keys_and_values():
    # Arrange: create several shapes
    shapes = [Square(2), Circle(1), Circle(3)]
    # Act: call area_stats
    stats = area_stats(*shapes)
    # Assert: stats is dict, has correct keys, and values are numbers
    assert isinstance(stats, dict)
    assert set(stats.keys()) == {"n", "total", "mean", "min", "max"}
    for value in stats.values():
        assert isinstance(value, (int,float))

def test_stats_raises_without_shapes():
    # Assert that calling area_stats() raises ValueError
    with pytest.raises(ValueError):
        area_stats()
