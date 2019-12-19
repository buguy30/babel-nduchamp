from year import validate_year

x = validate_year(1950)
print(f"retour {x} type {type(x)}")

x = validate_year("1950")
print(f"retour {x} type {type(x)}")

x = validate_year("1950xy")
print(f"retour {x} type {type(x)}")
exit(0)
