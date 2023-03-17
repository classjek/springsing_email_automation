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

# add circles in top left
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

# add circles to bottom right
rgb_color = 'rgb({}, {}, {})'.format(0, 59, 92)
drawing.add(drawing.circle(center=(650, 820), r=245, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(235, 236, 220)
drawing.add(drawing.circle(center=(650, 820), r=220, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(97, 156, 207)
drawing.add(drawing.circle(center=(650, 820), r=195, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(234, 194, 85)
drawing.add(drawing.circle(center=(650, 820), r=170, fill=rgb_color))
# next inner
rgb_color = 'rgb({}, {}, {})'.format(0, 59, 92)
drawing.add(drawing.circle(center=(650, 820), r=145, fill=rgb_color))

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

# adding text to it

manager = 'Manago'
celeb = 'celebo'

text = create_text("Manago", "celebo")
splext = text.split('\n')

y = 200
for line in splext:
    words = drawing.text(line, insert=(60, y), style = "font-size:11px; font-family:Arial")
    y += 7
    drawing.add(words)

drawing.save()

drawing = svg2rlg('letterhead3.svg')
renderPDF.drawToFile(drawing, 'file.pdf', autoSize=0)