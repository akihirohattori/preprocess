from astropy.io import fits
import re
from datetime import datetime
hdulist = fits.open("../../gra/HAY_A_AMICA_3_HAYAMICA_V1_0/data/20051028/st_2496903843_v.fit")
hdu = hdulist[0]
header = hdu.header
date = header["UTC_0"]
print(date)
date = re.split('[-T]',date)


l_year = 2003
l_month = 5
l_day = 9
l_date = datetime(l_year,l_month,l_day)

year = int(date[0])
month = int(date[1])
day = int(date[2])
date = datetime(year,month,day)

days = date - l_date

DAY = days.days
print(DAY)

B0 = 3.18 * pow(10,2)
B1 = -4.12 * pow(10,-2)
B2 = 2.00 * pow(10,-5)

I_BIAS = B0 + (B1 * DAY) + (B2 * pow(DAY,2))

print(I_BIAS)