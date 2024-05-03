def getNonUnityRow(extM: list[list[float]]) -> int:
    index   = 0
    row     = extM[index]
    while sum(row) == 0:
        index += 1
        row = extM[index]
    return index

def getDiagonals(extM: list[list[float]]) -> int:
    rows = len(extM)
    columns = len(extM[0])
    start = getNonUnityRow(extM)
    diagonals = ((extM[row-column][column] for column in range(columns)) for row in range(start, rows))
    return diagonals
    
def konvoluce(x: list[float], y: list[float]) -> list[float]:
    extender    = [[0 for mem in x] for _ in range(len(x)-1)]
    matrix      = extender + [[xi*yi for xi in x] for yi in y] + extender
    start       = getNonUnityRow(matrix)
    diagonals   = getDiagonals(matrix)
    return [sum(row) for row in diagonals]#[start//2:-start//2]

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-np.pi, np.pi, 361)
fx_1 = np.sin(x)
fx_2 = np.exp(x)/np.max(np.exp(x))
conv1 = np.convolve(fx_1, fx_2, mode="same")
conv2 = np.convolve(fx_2, fx_1, mode="same")
fig,ax = plt.subplots(2,1, sharex=True)
ax[0].plot(x, fx_1)
ax[0].plot(x, fx_2)
ax[1].plot(x, conv1)
ax[1].plot(x, conv2)
ax[0].grid()
ax[1].grid()
plt.show()