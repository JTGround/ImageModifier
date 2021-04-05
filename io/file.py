from numpy import save, savetxt


def save_array_as_bin(path, ar):
    save(path, ar)


def save_array_as_csv(path, ar):
    savetxt(path, ar, delimiter=',')