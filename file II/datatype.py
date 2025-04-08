"""
type: str
numeric types: int,float,complex
sequence types: list,tuple,range
mapping types: dict
set types: set,frozenset
boolean type: bytes,bytearray,memoryview
nonetype: nonetype

"""
a="hello"
print(type(a))  # <class 'str'>
b=20
print(type(b))
c=20.5
print(type(c))
d=1j
print(type(d))
e=["int","string","conc"]
f=("int","string","conc")
g=range(3)
h={'name':'John','age':30}
i=True
j=b"hi"
k=None
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
