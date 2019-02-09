def get_locs(ttc, btc, qty, hinge_ht, joh):
    top = ttc - (hinge_ht / 2)
    space = (joh - (ttc + btc)) / (qty - 1)
    hinges = [top]
    for i in range(1, qty):
        hinges.append(top + (i * space))
    return tuple(hinges)


def insert_builder(name, joh, hinge_qty, hinge_ht, locs):
    if hinge_qty == 3:
        h4 = "NULL"
    else:
        h4 = locs[3]
    return f"INSERT INTO hinge_locations (locations, joh, hinge_qty, hinge_size, h1, h2, h3, h4) VALUES ('{name.upper()}', {joh}, {hinge_qty}, {hinge_ht}, {locs[0]}, {locs[1]}, {locs[2]}, {h4});"
