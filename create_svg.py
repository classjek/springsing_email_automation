import svgwrite

# create a drawing 
drawing = svgwrite.Drawing('letterhead3.svg', size=(612, 792))
text = "Trial text 1"

# set background
r, g, b, = 217, 231, 242
rgb_color = 'rgb({}, {}, {})'.format(r, g, b)
drawing.add(svgwrite.shapes.Rect(insert=(0, 0), size=(700, 792), fill= rgb_color))

# circle in top left
drawing.add(drawing.circle(center=(200, 200), r=45, fill="red"))

# add circles in top left and bottom right
# outermost circle
rgb_color = 'rgb({}, {}, {})'.format(0, 59, 92)
drawing.add(drawing.circle(center=(0, -50), r=245, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(235, 236, 220)
drawing.add(drawing.circle(center=(0, -50), r=220, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(97, 156, 207)
drawing.add(drawing.circle(center=(0, -50), r=195, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(234, 194, 85)
drawing.add(drawing.circle(center=(0, -50), r=170, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(0, 59, 92)
drawing.add(drawing.circle(center=(0, -50), r=145, fill=rgb_color))

# add spring sing logo 
image = drawing.image(href='sing.png', insert=(325,-50), size=(275, 275))
drawing.add(image)

# add disco ball 
image = drawing.image(href='discoball.png', insert=(-145, -185), size=(300, 300))
drawing.add(image)



drawing.save()
