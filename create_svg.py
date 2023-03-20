import svgwrite

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


def create_text(manager, celeb):
    text = f"""
        Hello {manager}\n
        \n
        On behalf of the UCLA Student Alumni Association, it is our distinct honor to invite {celeb} to join our\n
        panel of celebrity judges and award presenters for Spring Sing 2023! \n
        \n
        Spring Sing is UCLA's oldest and greatest musical tradition, reaching back to entertainment's variety \n
        show roots. This annual event showcases our highest caliber of talented students through original \n
        performances of solo songs, duets, dance routines, and comedic sketches. With an audience of over \n
        6,000, we take great pride in selecting outstanding judges as examples of artistic achievement, \n
        creativity, and talent to continue to further the show's legacy. \n
        \n
        Spring Sing is where stars are made and stars return to celebrate the newest generation of artists.\n
        Notable past Spring Sing participants have included Adam Levine, Sara Bareilles, and Nasim Pedrad; \n
        former judges include Dennis Quaid, Kathy Bates, and Paula Abdul. \n
        \n
        Spring Sing will take place on Friday, May 19th, 2023 at UCLA. We ask that judges arrive at 6:00 pm \n
        for a reception, and attend the show to evaluate each act from 7:30pm to 9:30m. At the end of the \n
        night, judges will present an award to the respective recipients.  \n

        We hope you will join this year's team of judges and become a part of a tradition that continues to \n
        make Spring Sing the most anticipated UCLA event of the year. Thank you for your consideration\n
        and we would appreciate hearing back from you by March 30th, 2023. Please do not hesitate to\n
        email or call us at your convenience with any questions or concerns. \n
        \n
        Thank you for your time and we look forward to hearing from you soon! \n
        \n
        Best< \n
        \n
        Nikki Aviv & Charlotte Bradley \n
        Celebrity Engagement & Awards Directors | UCLA Spring Sing 2023 \n
        Phone: Nikki: (917) 471-4188 | Charlotte: (617) 818-6369 \n
        Email: judges.springsing@gmail.com \n
        Spring Sing - UCLA Alumni \n
         """

    return text

def create_dum(manager, celeb):
    text = 'a first line baby\n' + 'b\n' + f'c {celeb} blah blah\n' + f'a{manager}\n' + 'last one'
    return text
    


# create a drawing 
drawing = svgwrite.Drawing('letterhead3.svg', size=(612, 792))
text = "Trial text 1"

# set background
r, g, b, = 217, 231, 242
rgb_color = 'rgb({}, {}, {})'.format(r, g, b)
drawing.add(svgwrite.shapes.Rect(insert=(0, 0), size=(700, 792), fill= rgb_color))

radius = 200

# add circles in top left
# outermost circle
rgb_color = 'rgb({}, {}, {})'.format(0, 59, 92)
drawing.add(drawing.circle(center=(0, -50), r=radius, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(235, 236, 220)
drawing.add(drawing.circle(center=(0, -50), r=radius-25, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(97, 156, 207)
drawing.add(drawing.circle(center=(0, -50), r=radius-50, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(234, 194, 85)
drawing.add(drawing.circle(center=(0, -50), r=radius-75, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(0, 59, 92)
drawing.add(drawing.circle(center=(0, -50), r=radius-100, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(235, 236, 220)
drawing.add(drawing.circle(center=(0, -50), r=radius-125, fill=rgb_color))
# next inner, same color as background
rgb_color = 'rgb({}, {}, {})'.format(217, 231, 242)
drawing.add(drawing.circle(center=(0, -50), r=radius-150, fill=rgb_color))

# add circles to bottom right
rgb_color = 'rgb({}, {}, {})'.format(0, 59, 92)
drawing.add(drawing.circle(center=(650, 820), r=radius, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(235, 236, 220)
drawing.add(drawing.circle(center=(650, 820), r=radius-25, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(97, 156, 207)
drawing.add(drawing.circle(center=(650, 820), r=radius-50, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(234, 194, 85)
drawing.add(drawing.circle(center=(650, 820), r=radius - 75, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(0, 59, 92)
drawing.add(drawing.circle(center=(650, 820), r=radius-100, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(235, 236, 220)
drawing.add(drawing.circle(center=(650, 820), r=radius-125, fill=rgb_color))

# Add UCLA logo 
rgb_color = 'rgb({}, {}, {})'.format(17, 111, 160)
square = svgwrite.shapes.Rect(insert=(35, 740), size=('100px', '40px'), fill=rgb_color)
drawing.add(square)
#ucla = drawing.text('UCLA', insert=(64, 776), style = "font-size:27px; font-family:Greenwich-BoldItalic; font_weight:bold", fill='white', stroke='white', stroke_width="1")
xcord = 50
ycord = 769

ucla = drawing.text('U', insert=(xcord, ycord), font_family='Arial', style = "font-size:23px; font_weight:bold; italic;", fill='white', stroke='white', stroke_width='2')
drawing.add(ucla)
ucla = drawing.text('C', insert=(xcord+18, ycord), font_family='Arial', style = "font-size:23px; font_weight:bold; italic;", fill='white', stroke='white', stroke_width='2')
drawing.add(ucla)
ucla = drawing.text('L', insert=(xcord+36, ycord), font_family='Arial', style = "font-size:23px; font_weight:bold; italic", fill='white', stroke='white', stroke_width='2')
drawing.add(ucla)
ucla = drawing.text('A', insert=(xcord+52, ycord), font_family='Arial', style = "font-size:23px; font_weight:bold; italic", fill='white', stroke='white', stroke_width='2')
drawing.add(ucla)
alumni = drawing.text('Alumni', insert=(145, 771), font_family='Arial', style = "font-size:30px; font_weight:bold;", fill='black', stroke='black', stroke_width='1')
drawing.add(alumni)

# SAA logo brah
xcord = 268
ycord = 776
SAA = drawing.text('S', insert=(xcord, ycord), font_family='Arial', style = "font-size:60px; font_weight:bold; italic", fill='white', stroke='white', stroke_width='4')
drawing.add(SAA)
SAA = drawing.text('A', insert=(xcord+35, ycord), font_family='Arial', style = "font-size:60px; font_weight:bold; italic", fill='white', stroke='white', stroke_width='4')
drawing.add(SAA)
SAA = drawing.text('A', insert=(xcord+70, ycord), font_family='Arial', style = "font-size:60px; font_weight:bold; italic", fill='white', stroke='white', stroke_width='4')
drawing.add(SAA)


# Spring Sing Logo Brah
rgb_color = 'rgb({}, {}, {})'.format(17, 111, 160)
drawing.add(drawing.circle(center=(530, 100), r=45, fill=rgb_color))
rgb_color = 'rgb({}, {}, {})'.format(217, 231, 242)
twothree = drawing.text('2023', insert=(503, 109), font_family='Arial', style='font-size:25px; font_weight:bold;', fill=rgb_color, stroke=rgb_color, stroke_width='1.5')
drawing.add(twothree)
spring = drawing.text("Spring Sing", insert=(200, 200), font_family='Brush Script MT', style='font-size:60px;')
drawing.add(spring)


# this shit don't want to export 
"""
# add spring sing logo 
image = drawing.image(href='sing.png', insert=(325,-50), size=(275, 275))
drawing.add(image)

# add disco ball 
image = drawing.image(href='discoball.png', insert=(-145, -185), size=(300, 300))
drawing.add(image)
# second disco ball
image = drawing.image(href='discoball.png', insert=(490, 655), size=(300, 300))
drawing.add(image)

# add ucla alumni logo 
image = drawing.image(href='ucla_alum.png', insert=(0, 650), size=(200, 200))
drawing.add(image)
"""

# adding text to it

manager = 'Jake\'s Manger'
celeb = 'Shaan Goel'

text = create_text(manager, celeb)
splext = text.split('\n')

y = 200
for line in splext:
    words = drawing.text(line, insert=(60, y), style = "font-size:11px; font-family:Arial")
    y += 7
    drawing.add(words)

drawing.save()

