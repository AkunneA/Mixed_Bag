from PyShapes import *
shapes = PyShape("shapes.png")

shapes_dictionary = shapes.get_all_shapes()
print(shapes_dictionary)
shapes.show_shapes()

print(shapes.get_corners("triangle", 1))
shapes.close()
