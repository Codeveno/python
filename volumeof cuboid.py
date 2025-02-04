# declare values
#l = 5
#w = 3
#h =  4

l=int(input("kindly enter the length"))
w=int(input("kindly enter the width"))
h=int(input("kindly enter the height"))

#finding volume of cuboid
def volumeofcuboid(l, w, h):
    if h <= 0:
        return "Height should be greater than 0"
    volume = l * w * h
    return f"{volume:7f}"

#func call
result = volumeofcuboid(l, w, h)
print(result)