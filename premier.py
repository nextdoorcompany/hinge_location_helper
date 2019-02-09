import hinge_location_helper as h

print("use engineering;\n")

for joh in (80, 86):
    for hinge_ht in (4.5, 5):
        print(
            h.insert_builder(
                "PREMIER", joh, 3, hinge_ht, h.get_locs(7.25, 12.25, 3, hinge_ht, joh)
            )
        )

for joh in (90, 96):
    for hinge_ht in (4.5, 5):
        print(
            h.insert_builder(
                "PREMIER", joh, 4, hinge_ht, h.get_locs(7.25, 12.25, 4, hinge_ht, joh)
            )
        )
