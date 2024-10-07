t=2,4,5,6,6,7
print(t)
t=t+(2,)
print(t)
l=list(t)
l.append(3)
t=tuple(l)
print(t)
print: t[1]