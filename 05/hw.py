import re
p = re.compile(r"\\includegraphics ( \[ [^\]]+ \] )? \{ ( [^}]+ ) \} ", re.VERBOSE)

for l in open("Gvaramadze2010.tex"):
    l = l.split("%")[0]
    m = p.search(l)
    if m:
        print m.groups()

