nonsense = "blog trust fund tattooed williamsburg poke roof party"
has_ok = "ok" in nonsense

if has_ok:
    print("yeet")
elif len(nonsense) > 10:
    print("yo")
else:
    print("no")

has_zoo = "zoo" in nonsense
has_fun = "fun" in nonsense

if has_zoo and has_ok:
    print("cool")
elif has_ok:
    print("rad")
elif has_fun:
    print("dope")
else:
    print("nope")



q = 25
if q % 3 == 0 and q % 5 == 0:
    print("both")
elif q % 3 == 0 or q % 5 == 0:
    print("either")
else:
    print("neither")

r = 9
if r % 3 == 0 and r % 5 == 0:
    print("both")
elif r % 3 == 0 or r % 5 == 0:
    print("either")
else:
    print("neither")

s = 15
if s % 3 == 0 and s % 5 == 0:
    print("both")
elif s % 3 == 0 or s % 5 == 0:
    print("either")
else:
    print("neither")

