from numpy import nditer


def bleachmanual(arr, white_pt):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i, j] > white_pt:
                arr[i, j] = 255
            else:
                arr[i, j] = 0


def bleach(arr, white_pt):
    with nditer(arr, op_flags=['readwrite']) as it:
        for x in it:
            if x > white_pt:
                x[...] = 255
            else:
                x[...] = 0


def blot(arr):
    with nditer(arr, op_flags=['readwrite']) as it:
        for x in it:
            if x < 255:
                x[...] = 1


def removeptrange(arr, numpix):
    blackpt = 0
    xlen = len(arr)
    for x in range(xlen):
        ylen = len(arr[x])
        for y in range(ylen):
            if x - numpix > 0 and y - numpix > 0 and x+numpix < xlen and y+numpix < ylen:
                if arr[x-numpix, y] > blackpt and arr[x+numpix, y] > blackpt \
                        and arr[x, y-numpix] > blackpt and arr[x, y+numpix] > blackpt \
                        and arr[x-numpix, y-numpix] > blackpt and arr[x-numpix, y+numpix] > blackpt \
                        and arr[x+numpix, y-numpix] > blackpt and arr[x+numpix, y+numpix] > blackpt:
                    x1 = x-numpix
                    x2 = x+numpix
                    y1 = y-numpix
                    y2 = y+numpix
                    for xpix in range(x1, x2):
                        for ypix in range(y1, y2):
                            arr[xpix, ypix] = 255
