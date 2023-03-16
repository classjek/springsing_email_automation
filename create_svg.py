import svgwrite

# create a drawing 
drawing = svgwrite.Drawing('letterhead3.svg', size=(612, 792))
text = "Trial text 1"

# set background
r, g, b, = 217, 231, 242
rgb_color = 'rgb({}, {}, {})'.format(r, g, b)
drawing.add(svgwrite.shapes.Rect(insert=(0, 0), size=(612, 792), fill= rgb_color))

# circle in top left
drawing.add(drawing.circle(center=(200, 200), r=45, fill="red"))

# add cirlces in top left and bottom right



drawing.save()
