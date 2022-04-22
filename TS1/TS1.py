import numpy as np
from matplotlib import pyplot as plt

# módulo de SciPy
from scipy import signal as sig

# Agrego funciones que voy a usar de splane
from splane import bodePlot, pzmap

# Defino valores de componentes
R1 = 1000
R2 = 1000
Rn = R2/R1

# Defino numerador y denominador
num = np.array([1,-Rn])
den = np.array([1,1])

# Obtengo transferencia
H_s = sig.TransferFunction(num,den)

# Ploteo
plt.close('all')
bodePlot(H_s, [-3,3], [-3,3])

# Diagrama de polos y ceros
pzmap(H_s)

