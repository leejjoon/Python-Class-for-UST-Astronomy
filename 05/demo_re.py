import re

p = re.compile(r"06Mar[0-9][0-9][0-9]\.fits")

for s in ["06Mar000.fits", "06Mar001.fits", "06Mar999.fits"]:
  assert p.match(s)

for s in ["06Mar00.fits", "06Mar0010fits", "06Mar999.fit"]:
  assert not p.match(s)

p = re.compile(r"[*^]")

for s in ["^", "*"]:
  assert p.match(s)


p = re.compile(r"ab?c")

for s in ["abc", "ac"]:
  assert p.match(s)


p = re.compile(r"a\d\d?")

for s in ["a0", "a01"]:
  assert p.match(s)

p = re.compile(r"06Mar(\d+)\.fit")
m1 = p.match("06Mar1232.fit") # m1.group() => '06Mar1232.fit'
m2 = p.match("06Mar1232.fits") # m1.group() => '06Mar1232.fit'
m3 = p.match("2012_06Mar1232.fits") # None
m4 = p.search("2012_06Mar1232.fits") # None

print m1.group(), m1.groups()

p = re.compile('section{ ( [^}]* ) }', re.VERBOSE)
s = p.sub(r'subsection{\1}','section{First} section{second}')
# 'subsection{First} subsection{second}'

p = re.compile(r"(fits|FITS)")
assert p.search("a.fits")
assert p.search("A.FITS")
assert not p.search("av.Fits")

