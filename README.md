# MaNGA_High_Order_stellar_kinematic
The stellar kinematic moments (V, $\sigma$, $h_3$, $h_4$) on a sample of 2, 230 galaxies with $\sigma_e$ > 140km/s in the final data release of the MaNGA survey.

## Kinematic Data

The `kinematics` folder contains the kinematic data of 2230 galaxies, with the data format shown below. For each galaxy, the Header Data Unit (HDU) in which it is stored, the name, its dimensions, units, and a brief description are presented. The properties with prefix `DAP` are taken from the DAP MAPS file ([Section 12.1 in DAP](https://ui.adsabs.harvard.edu/abs/2019AJ....158..231W/abstract)).

| HDU | Name | Dimensions | Units | Description |
|-----|------|------------|-------|-------------|
| 0   | Primary |  |  | Empty primary header |
| 1   | DAP_SPX_SKYCOO | (N, N, 2) | arcsec | Sky-right offsets (+x toward +RA, +y toward +DEC) of each spaxel from the galaxy center. Same as `SPX_SKYCOO` in the corresponding MAPS file. |
| 2   | DAP_SPX_MFLUX | (N, N) | 10^-17 erg/s/cm²/Å/spaxel | g-band-weighted mean flux, not corrected for Galactic extinction or internal attenuation. Same as `SPX_MFLUX` in the corresponding MAPS file. |
| 3   | BINID | (N, N) |  | Numerical ID for spatial bins binned to S/N = 30 |
| 4   | Stellar_Vel_Gauss | (N, N) | km/s | Gaussian line-of-sight stellar velocity derived with moments=2. |
| 5   | Stellar_Vel_Ivar_Gauss | (N, N) |  | Inverse variance in Stellar_Vel_Gauss. |
| 6   | Stellar_Sigma_Gauss | (N, N) | km/s | Gaussian line-of-sight stellar velocity dispersion derived with moments=2. |
| 7   | Stellar_Sigma_ivar_Gauss | (N, N) |  | Inverse variance in Stellar_Sigma_Gauss. |
| 8   | Stellar_Vel_GH | (N, N) | km/s | Line-of-sight stellar velocity derived from fitting four kinematic moments (V, σ, h₃, h₄) with moments=4. |
| 9   | Stellar_Vel_Ivar_GH | (N, N) |  | Inverse variance in Stellar_Vel_GH. |
| 10  | Stellar_Sigma_GH | (N, N) | km/s | Line-of-sight stellar velocity dispersion derived from fitting four kinematic moments (V, σ, h₃, h₄) with moments=4. |
| 11  | Stellar_Sigma_ivar_GH | (N, N) |  | Inverse variance in Stellar_Sigma_GH. |
| 12  | Stellar_h3_GH | (N, N) |  | Line-of-sight stellar h₃ derived from fitting four kinematic moments (V, σ, h₃, h₄) with moments=4. |
| 13  | Stellar_h3_ivar_GH | (N, N) |  | Inverse variance in Stellar_h3_GH. |
| 14  | Stellar_h4_GH | (N, N) |  | Line-of-sight stellar h₄ derived from fitting four kinematic moments (V, σ, h₃, h₄) with moments=4. |
| 15  | Stellar_h4_ivar_GH | (N, N) |  | Inverse variance in Stellar_h4_GH. |


## Example: Plotting Kinematic Maps

The script `plot_kinematic_map.py` provides an example of how to plot the corresponding maps of  
(V, $\sigma$, $h_3$, $h_4$) for a given MaNGAID.  

Running this example will generate the file `kinematic_map_1-44526.png` in the `example` folder.  

## Stellar Library

The file `Mastar_hierarchical_clusters.fits` contains the stellar library used to obtain these kinematic data.  

Users can refer to the example in `plot_stellar_lib.py` to read the templates from the stellar library.  
These templates are **normalized by their median value**.  

Running `plot_stellar_lib.py` will generate the figure `Template-stars.png` in the `example` folder.
