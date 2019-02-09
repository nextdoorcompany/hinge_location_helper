import hinge_location_helper as h


def test_locs_three():
    result = h.get_locs(7.25, 12.25, 3, 4.5, 84)
    assert result == (5, 37.25, 69.5)


def test_locs_four():
    result = h.get_locs(7.25, 12.25, 4, 4.5, 84)
    assert result == (5, 26.5, 48, 69.5)
