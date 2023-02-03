i = 0


def counting():
    global i
    i += 1
    return i


def tower_of_hanoi(numdisks, frm_disc, to_disc, aux_disc):
    if numdisks == 1:
        print(f"{counting()}. Move disk [1] from rod [{frm_disc}] to rod [{to_disc}] ")
        return

    tower_of_hanoi(numdisks - 1, frm_disc, aux_disc, to_disc)

    print(f"{counting()}. Move disk [{numdisks}] from rod [{frm_disc}] to rod {to_disc}]")
    tower_of_hanoi(numdisks - 1, aux_disc, to_disc, frm_disc)


numdisks = int(input("INPUT NUMBER OF DISKS: "))
tower_of_hanoi(numdisks, "A", "C", "B")
