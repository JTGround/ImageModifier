from numpy import nditer


def filter_pts(arr):
    with nditer(arr, op_flags=['readwrite'], flags=['f_index']) as it:
        for x in it:
            index = it.index
            print(index)