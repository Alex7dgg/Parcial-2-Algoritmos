import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------
#       SISTEMA DE ECUACIONES DE LORENZ
# -------------------------------------------------------------
def lorenz(x, y, z, sigma, rho, beta):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

# -------------------------------------------------------------
#       MÉTODO RUNGE–KUTTA DE 4º ORDEN
# -------------------------------------------------------------
def rk4_step(x, y, z, dt, sigma, rho, beta):
    k1 = lorenz(x, y, z, sigma, rho, beta)
    k2 = lorenz(x + dt*k1[0]/2, y + dt*k1[1]/2, z + dt*k1[2]/2, sigma, rho, beta)
    k3 = lorenz(x + dt*k2[0]/2, y + dt*k2[1]/2, z + dt*k2[2]/2, sigma, rho, beta)
    k4 = lorenz(x + dt*k3[0],   y + dt*k3[1],   z + dt*k3[2],   sigma, rho, beta)

    x_new = x + dt*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0]) / 6
    y_new = y + dt*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1]) / 6
    z_new = z + dt*(k1[2] + 2*k2[2] + 2*k3[2] + k4[2]) / 6

    return x_new, y_new, z_new

# -------------------------------------------------------------
#       SIMULACIÓN DE UNA TRAYECTORIA
# -------------------------------------------------------------
def simulate_lorenz(x0, y0, z0, sigma, rho, beta, dt=0.01, T=100):
    steps = int(T/dt)
    xs = np.zeros(steps)
    ys = np.zeros(steps)
    zs = np.zeros(steps)

    x, y, z = x0, y0, z0
    for i in range(steps):
        xs[i], ys[i], zs[i] = x, y, z
        x, y, z = rk4_step(x, y, z, dt, sigma, rho, beta)

    return xs, ys, zs

# -------------------------------------------------------------
#       FUNCIÓN PARA GRAFICAR 10 TRAYECTORIAS
# -------------------------------------------------------------
def plot_simulation(params, title):
    sigma, rho, beta = params
    fig = plt.figure(figsize=(10,7))
    ax = fig.add_subplot(111, projection='3d')

    # 10 condiciones iniciales distintas
    initial_points = np.random.uniform(-10, 10, (10, 3))

    for (x0,y0,z0) in initial_points:
        xs, ys, zs = simulate_lorenz(x0, y0, z0, sigma, rho, beta)
        ax.plot(xs, ys, zs, linewidth=1)

    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.tight_layout()
    plt.show()

# -------------------------------------------------------------
#       SIMULACIÓN BASE (σ=10, ρ=28, β=8/3)
# -------------------------------------------------------------
plot_simulation((10, 28, 8/3), "Sistema de Lorenz – Parámetros clásicos")

# -------------------------------------------------------------
#       VARIACIÓN DE PARÁMETROS (3 escenarios)
# -------------------------------------------------------------
plot_simulation((14, 28, 8/3), "Variación 1: σ aumentado (σ=14)")
plot_simulation((10, 35, 8/3), "Variación 2: ρ aumentado (ρ=35)")
plot_simulation((10, 28, 3.5), "Variación 3: β aumentado (β=3.5)")
