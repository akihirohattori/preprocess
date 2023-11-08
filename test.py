from astropy.io import fits
import numpy as np



alpha = {"ul":1.26,"b":1.28,"v":1.41,"w":1.85,"x":1.85,"p":1.60,"zs":1.48}

hdulist = fits.open("../../gra/HAY_A_AMICA_3_HAYAMICA_V1_0/data/20050929/st_2418807291_p.fit")
hdu = hdulist[0]
data = hdu.data
header = hdu.header
filter = header["FILTER_0"]

print(filter+".fit")
a=np.array([0,0])
b=np.array([512,512])
distance=np.linalg.norm(b-a)
print(distance)

# sum = 0
# count = 0
# for x in range(header["NAXIS1"]):
#     for y in range(header["NAXIS2"]):
#         if(data[x][y]>1000):
#             sum = sum + data[x][y]
#             count+=1

# ave = sum/count
# print(ave)