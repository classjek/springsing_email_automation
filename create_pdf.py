import svgwrite

dwg = svgwrite.Drawing('letterhead2.svg')

dwg.add(dwg.text('', insert=(50, 50)))

dwg.save()


