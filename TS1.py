import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

# módulo de SciPy
from scipy import signal as sig

# Agrego funciones que voy a usar de splane
from splane import bodePlot

# Defino valores de componentes
R1 = 1000
R2 = 1000

# Defino numerador y denominador
num = np.array([1,-R2/R1])
den = np.array([1,1])

# Obtengo transferencia
H_s = sig.TransferFunction(num,den)

# Ploteo
plt.close('all')
bodePlot(H_s, [-3,3], [-3,3])

