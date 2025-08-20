

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
templates = fits.open('Mastar_hierarchical_clusters.fits')
wavelength = templates['Wavelength'].data #wavelength in Angstrom
stars = templates['Template_flux'].data #stellar templates
plt.figure(figsize=(8,25))
grid = plt.GridSpec(27, 2)
for i in range(27):
    ax=plt.subplot(grid[i,0])
    plt.plot(wavelength,stars[:,i],c='k',linewidth=1)
    if i%2 == 1:
        ax.set_facecolor('#F0F0F0')
    if i !=26:
        plt.xticks([])
    else:
        plt.xlabel(r'Wavelength [$\rm \AA$]',size=15)
    ymin, ymax = plt.ylim()
    yticks_pos = [ymin, (ymin + ymax)/2]
    yticks_labels = [0, 1]
    plt.yticks(yticks_pos, yticks_labels)
for i in range(27,54):
    ax=plt.subplot(grid[i%27,1])
    plt.plot(wavelength,stars[:,i],c='k',linewidth=1)
    if i%2 == 0:
        ax.set_facecolor('#F0F0F0')
    if i !=53:
        plt.xticks([])
    else:
        plt.xlabel(r'Wavelength [$\rm \AA$]',size=15)
    plt.yticks([])
plt.subplots_adjust(wspace=0,hspace=0)
plt.savefig('Template-stars.png')
plt.close()