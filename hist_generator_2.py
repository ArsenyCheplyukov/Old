import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

array = np.array(np.loadtxt('./data/1ms/frequency84Mhz.txt', dtype=float))
print(array.min())