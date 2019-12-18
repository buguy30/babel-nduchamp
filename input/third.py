from second import validate_display, validate, validate_string
from second import F_ERROR

print("THIRD")

d = validate("Essai Deux")
if F_ERROR in d:
    print(d[F_ERROR])
print(d)

"""
print("-" * )
d = validate("")
if F_ERROR in d:
    print(d[F_ERROR])
print(d)


d = validate("Emmanuel Sandorfi")
if F_ERROR in d:
    print(d[F_ERROR])
print(d)
"""
