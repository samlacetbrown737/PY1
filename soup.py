def soupTop(radius):
	return 2.0*3.1415926535*(float(radius)*float(radius))
def soupLabel(radius, height):
	return 2.0*3.1415926535*float(radius)*float(height)
def soupCan(radius, height):
	return("Total Area: " + str(soupLabel(radius,height)+soupTop(radius)) + "\nTop/Bottom: " + str(soupTop(radius)) + "\nLabel Area: " + str(soupLabel(radius,height)))
r = input("Radius? ")
h = input("Height? ")
print(soupCan(r,h))
