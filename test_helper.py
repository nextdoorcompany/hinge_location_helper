import hinge_location_helper as h


def test_locs_three():
    result = h.get_locs(7.25, 12.25, 3, 4.5, 84)
    assert result == (5, 37.25, 69.5)


def test_locs_four():
    result = h.get_locs(7.25, 12.25, 4, 4.5, 84)
    assert result == (5, 26.5, 48, 69.5)


def test_insert_builder_three():
    result = h.insert_builder("fcf", 84, 3, 4.5, (5, 37.25, 69.5))
    assert (
        result
        == "INSERT INTO hinge_locations (locations, joh, hinge_qty, hinge_size, h1, h2, h3, h4) VALUES ('FCF', 84, 3, 4.5, 5, 37.25, 69.5, NULL);"
    )


def test_insert_builder_four():
    result = h.insert_builder("fcf", 84, 4, 4.5, (5, 26.5, 48, 69.5))
    assert (
        result
        == "INSERT INTO hinge_locations (locations, joh, hinge_qty, hinge_size, h1, h2, h3, h4) VALUES ('FCF', 84, 4, 4.5, 5, 26.5, 48, 69.5);"
    )
