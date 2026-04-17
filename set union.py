setc1 = {"green","blue"}
setc2 = {"blue","yellow"}
print("Original sets:")
print(setc1)
print(setc2)
setc = setc1.union(setc2)
print("\nUnion of above sets:")
print(setc)

setx = {"green","blue"}
sety = {"blue","yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets")
setz = setx.intersection(sety)
print(setz)