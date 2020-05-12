"""
AACSE_pymap.py
Recreate and improve my station map from Matlab in Python. Part of Parker
MacCready's Effective Computing course
"""

# imports
import sys, os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import netcdf
import cmocean

# local imports
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
this_parent, out_dir = mymod.get_outdir()
mymod.make_dir(out_dir)

# station details
good_lat = np.array([54.3715, 54.9200, 54.8830, 54.5150, 54.9000, 54.6711])
good_lon = np.array([-155.0717, -155.2550, -155.9170, -156.2500, -157.3670,
    -157.4156])
good_name = ['LA21', 'LA23', 'LA25', 'LA26', 'LA28', 'LA30']

bad_lat = np.array([53.9855, 54.2920])
bad_lon = np.array([-156.6320, -157.3670])
bad_name = ['LA27', 'LA29']

miss_lat = np.array([54.5674])
miss_lon = np.array([-160.2019])
miss_name = ['LT17']

# read .nc file
file2read = netcdf.NetCDFFile('../EffComp_data/AACSE_etopo1_bedrock.nc','r')
temp = file2read.variables['lat']
lat = temp[:]*1
temp = file2read.variables['lon']
lon = temp[:]*1
temp = file2read.variables['Band1']
elev = temp[:]*1

# plotting
XX, YY = np.meshgrid(lon,lat)

# PLOTTING
fs = 14 # primary fontsize
lw = 3 # primary linewidth
mk = 10 # primary markersize
plt.close('all')

fig = plt.figure(figsize=(12,10))

# ----------------------------------------------------------------------

cmap = cmocean.cm.topo
ax = fig.add_subplot(111)
cs = ax.pcolormesh(XX,YY, elev, cmap=cmap, vmin=-6000, vmax=6000)
gd = ax.plot(good_lon, good_lat, '^', markerfacecolor='gold',
    markeredgecolor='black', markersize=mk, label='Available')
bd = ax.plot(bad_lon, bad_lat, 'v', markerfacecolor='crimson',
    markeredgecolor='black',markersize=mk, label='Failed')
ms = ax.plot(miss_lon, miss_lat, '^', markeredgecolor='black',
    markerfacecolor='none', markersize=mk, markeredgewidth=2, label='Missing')

ax.axis('square')
ax.set_xlim((-161,-153))
ax.set_ylim((52, 58))
ax.grid(True)
ax.legend(loc='lower right')
ax.set_title('AACSE Station Map', weight='bold', fontsize=fs+2)
ax.tick_params(labelsize=fs)

cb = fig.colorbar(cs)
cb.set_label('Depth (m)', fontsize=fs)
cb.ax.tick_params(labelsize=fs)

plt.show()
