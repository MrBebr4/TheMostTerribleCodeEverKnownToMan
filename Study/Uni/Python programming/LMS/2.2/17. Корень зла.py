a = float(input())
b = float(input())
c = float(input())

discriminant = b ** 2 - 4 * a * c
if discriminant < 0:
    print("No roots")
    quit()
root1 = -b +  discriminant ** 1/2 / (2 * a)
root2 = -b - discriminant ** 1/2 / (2 * a)

if root1 == root2:
    print(root1)
else:
    print(root2, root1)
