import numpy as np
import matplotlib.pyplot as plt

#Frequency range
omega = np.linspace(-10,10,1000)

#Resonance frequency
omega_0 = 0

#Different dephasing rates (gamma = 1/T2)
gammas = [0.5,1.0,2.0]

plt.figure(figsize=(8,6))
for gamma in gammas:
    I = gamma/((omega - omega_0)**2 + gamma**2)
    plt.plot(omega, I, linewidth=2, label =f'$\gamma$={gamma}')

plt.title('Lorentzian Lineshape (Effect of Dephasing)')
plt.xlabel("$Frequency (\omega)$")
plt.ylabel("Intensity(a.u.)")
plt.legend()
plt.grid()
plt.show()

plt.savefig("output.png", dpi = 300)