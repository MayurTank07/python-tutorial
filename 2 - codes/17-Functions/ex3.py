## Arbitrary Arguments, *args

# def persons(*names):
#     print(f"Name is {names[0]}")
#     print(f"Name is {names[1]}")

# persons("dex", "chlore")

## Keyword Arguments

# def persons(p1, p2, p3):
#     print(f"Person 1 is {p1}")
#     print(f"Person 2 is {p2}")
#     print(f"Person 3 is {p3}")
    

# persons(p3="krystal", p1="dex", p2="chlore")


# Arbitrary Keyword Arguments, **kwargs

# def persons(**names):
#     print(f"Person 1 is {names["p1"]}")
#     print(f"Person 2 is {names["p2"]}")
#     print(f"Person 3 is {names["p3"]}")
    

# persons(p3="krystal", p1="dex", p2="chlore")

#Default parameter

# def persons(name = "none"):
#     print(f"Person name is {name}")

# persons("dex")
# persons("chlore")
# persons()
# persons("krystal")