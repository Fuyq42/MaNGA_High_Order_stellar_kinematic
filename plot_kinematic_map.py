from astropy.io import fits
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from astropy.io import fits
from plotbin.sauron_colormap import register_sauron_colormap
from mpl_toolkits.axes_grid1 import make_axes_locatable
register_sauron_colormap()
def extract_kinematic_maps(mangaid):
    
    data = fits.open('kinematics/'+mangaid+'.fits')
    V = data['Stellar_Vel_GH'].data
    S = data['Stellar_Sigma_GH'].data
    h3 = data['Stellar_h3_GH'].data
    h4 = data['Stellar_h4_GH'].data
    flux = data['DAP_SPX_MFLUX'].data
    size = V.shape[0]
    center = int(size / 2)

    return V, S, h3, h4,size,center,flux

mangaid = '1-44526'
V, S, h3, h4, size, center,flux = extract_kinematic_maps(mangaid)

fig = plt.figure(figsize=(17,4 ))
grid = plt.GridSpec(1, 4)
ax4 = fig.add_subplot(grid[0, 0])
plt.imshow(V, cmap='sauron', origin='lower',vmin = -150, vmax = 150)
x = np.arange(0, size, 1)
y = np.arange(0, size, 1)
X, Y = np.meshgrid(x, y)
plt.contour(X, Y, flux,colors='m',linewidths = 2,levels=[0.1*np.max(flux),0.2*np.max(flux),0.5*np.max(flux)])
ticks = np.concatenate((np.arange(center, 0, -10),np.arange(center + 10, 2 * center , 10)))
plt.xticks(ticks=ticks,labels=((ticks-center)/2).astype(int))
plt.yticks(ticks=ticks,labels=((ticks-center)/2).astype(int))
ax4.tick_params(axis='x', direction='in', pad=3)
ax4.tick_params(axis='y', direction='in', pad=3)
plt.xlim(0,2*center)
plt.ylim(0,2*center)
plt.text(3,3,'V',size=20)
plt.text(3,size-3.5,'-150/150 km/s',size=15)
plt.xlabel(r'arcsecond',size=15)
plt.ylabel(r'arcsecond',size=15)
ax4.set_aspect('equal')
ax5 = fig.add_subplot(grid[0, 1])
plt.imshow(S, cmap='sauron', origin='lower',vmin = 80, vmax = 150)
plt.contour(X, Y, flux,colors='m',linewidths = 2,levels=[0.1*np.max(flux),0.2*np.max(flux),0.5*np.max(flux)])
plt.xticks(ticks=ticks,labels=((ticks-center)/2).astype(int))
ax5.tick_params(axis='x', direction='in', pad=3)
plt.yticks([])
plt.xlim(0,2*center)
plt.ylim(0,2*center)
plt.text(3,3,r'$\rm \sigma$',size=20)
plt.text(3,size-3.5,'80/150 km/s',size=15)
plt.xlabel(r'arcsecond',size=15)
ax5.set_aspect('equal')
ax6 = fig.add_subplot(grid[0, 2])
plt.imshow(h3, cmap='sauron', origin='lower',vmin = -0.1, vmax = 0.1)
plt.contour(X, Y, flux,colors='m',linewidths = 2,levels=[0.1*np.max(flux),0.2*np.max(flux),0.5*np.max(flux)])
plt.xticks(ticks=ticks,labels=((ticks-center)/2).astype(int))
ax6.tick_params(axis='x', direction='in', pad=3)
plt.yticks([])
plt.xlim(0,2*center)
plt.ylim(0,2*center)
plt.text(3,3,r'$\rm h_3$',size=20)
plt.text(3,size-3.5,'-0.15/0.15',size=15)
plt.xlabel(r'arcsecond',size=15)
ax6.set_aspect('equal')
ax7 = fig.add_subplot(grid[0, 3])
plt.imshow(h4, cmap='sauron', origin='lower',vmin = -0.15, vmax = 0.15)
plt.contour(X, Y, flux,colors='m',linewidths = 2,levels=[0.1*np.max(flux),0.2*np.max(flux),0.5*np.max(flux)])
plt.xticks(ticks=ticks,labels=((ticks-center)/2).astype(int))
ax7.tick_params(axis='x', direction='in', pad=3)
plt.yticks([])
plt.xlim(0,2*center)
plt.ylim(0,2*center)
plt.text(3,3,r'$\rm h_4$',size=20)
plt.text(3,size-3.5,'-0.15/0.15',size=15)
plt.xlabel(r'arcsecond',size=15)
ax7.set_aspect('equal')
divider = make_axes_locatable(ax7)
mapple = matplotlib.cm.ScalarMappable(cmap='sauron')
cax = divider.append_axes("right", size="5%", pad=0)
cb = plt.colorbar(mapple,cax=cax,ticks=[])
plt.savefig('kinematic_map_'+mangaid+'.png')
plt.close()
