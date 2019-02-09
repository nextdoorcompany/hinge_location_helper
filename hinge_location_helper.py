def get_locs(ttc, btc, qty, hinge_ht, joh):
    top = ttc - (hinge_ht / 2)
    space = (joh - (ttc + btc)) / (qty - 1)
    hinges = [top]
    for i in range(1, qty):
        hinges.append(top + (i * space))
    return tuple(hinges)
