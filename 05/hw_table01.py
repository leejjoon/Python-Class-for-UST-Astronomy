import re
p = re.compile(r"\\includegraphics ( \[ [^\]]+ \] )? \{ ( [^}]+ ) \} ", re.VERBOSE)

for l in open("Gvaramadze2010.tex"):
    l = l.split("%")[0]
    if l.startswith(r"MN\qq"):
        n, ra, dec = l.split("&")[:3]
        h, m, s = ra.split()
        ra_deg = (float(h)+float(m)/60+float(s)/3600.)/24.*360.

        d, m, s = dec.split()
        if d[0] == "-":
            d=d[1:]
            dec_sign = -1
        else:
            dec_sign = 1
        dec_deg = dec_sign*(float(d)+float(m)/60+float(s)/3600.)

        print "{:.8} {:.8}".format(ra_deg, dec_deg)

