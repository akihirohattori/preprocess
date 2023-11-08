from astropy.io import fits
import numpy as np

hdulist = fits.open("../../gra/HAY_A_AMICA_3_HAYAMICA_V1_0/data/20051014/st_2458916352_w.fit")
hdu = hdulist[0]
data = hdu.data
header = hdu.header

ISKY = 300
NV = header["NAXIS1"]
NH = header["NAXIS2"]
tEXP = header["EXP_0"]
tVCT = 12 * NV #μs

I = np.zeros((256,256))

for H in range (NH):
    Ismear = 0
    for V in range (NV):
        Ismear = Ismear + (tVCT / (tVCT + tEXP)) * ((data[V,H] - ISKY)/NV)
    I[:,H] = data[:,H] - Ismear

hdu = fits.PrimaryHDU(I)
hdulist = fits.HDUList([hdu])
hdulist.writeto('smear_n.fits',overwrite=True)