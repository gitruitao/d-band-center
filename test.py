import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{times}'

plt.figure()
plt.xlabel(r'$E-\mathrm{E_f}$ / eV')
plt.ylabel('Sum of specified columns')
plt.title('Electronic Density of States')
plt.grid(True)
plt.show()
