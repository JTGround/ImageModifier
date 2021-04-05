from numpy import nditer


def drawhor(arr, ypt):
    for col in range(len(arr[ypt])):
        arr[ypt, col] = 80


def drawvert(arr, xpt):
    for row in range(len(arr)):
        arr[row, xpt] = 80


def drawgrid(arr, skip):
    drawhor(arr, skip)
    drawvert(arr, skip)
