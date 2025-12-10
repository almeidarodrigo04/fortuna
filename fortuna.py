""" 
    COMO RODAR:

    uv sync (primeira vez)
    uv run fortuna.py

    lembrar de ajustar parametros a cada vez
"""

import numpy as np
import matplotlib.pyplot as plt

RADIUS = 1

def get_point(n, plot):
    if plot:
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

    points = []
    for i in range(n):
        theta = np.random.rand() * 2 * np.pi
        # maracutaia geminiana, se vc gerar phi uniformemente n fica uniforme na esfera
        cos_phi = 2 * np.random.rand() - 1 
        sin_phi = np.sqrt(1 - cos_phi**2) # sin^2(phi) + cos^2(phi) = 1

        x = RADIUS * np.cos(theta) * sin_phi
        y = RADIUS * np.sin(theta) * sin_phi
        z = RADIUS * cos_phi

        if plot: ax.scatter(x, y, z)

        points.append((x, y, z))

    if plot:
        ax.set_aspect('equal')
        plt.show()
        plt.close()
    
    return np.array(points)

def check_win(p):
    # sisteminha de equação bolado
    P = np.array([p[0], p[1], p[2], p[3]]).T
    A = np.vstack([P, [1, 1, 1, 1]])
    b = np.array([0, 0, 0, 1])
    alpha = np.linalg.solve(A, b)
    if np.all(alpha >= -1e-9):
            return 1
    return 0

# Aqui vc escolhe a quantidade de pontos
N=int(1e6)

# Lembra de falar se vc quer ou n plotar (só precisa pro primeiro passo)
points = get_point(N, False)

p_chapeu = 0
for i in range(N//4):
    pontos= [points[i*4+j] for j in range(4)]
    p_chapeu += check_win(pontos)

print(p_chapeu/N)


