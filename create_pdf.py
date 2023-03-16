import PyPDF2

# Open the PDF file you want to add text to
pdf_file = open('createpdf.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the first page of the PDF
page = pdf_reader.pages[0]

# Create a PDF writer object
pdf_writer = PyPDF2.PdfWriter()

# Add the page to the writer object
pdf_writer.add_page(page)

# Create a new PDF object to add text to
new_pdf = PyPDF2.PdfReader(open('createpdf.pdf', 'rb'))

# Get the page you want to add text to
page = new_pdf.pages[0]

# Create a PDF canvas object
canvas = PyPDF2.pdf.ContentStream([PyPDF2.pdf.pdfname.BaseFont("Helvetica-Bold"), 14])

# Set the position of the text on the page
x = 100
y = 500

# Set the text you want to add to the page
text = "Hello, World!"

# Draw the text on the canvas
canvas.drawString(x, y, text)

# Add the canvas to the page
page.mergeContentStreams(canvas)

# Write the new PDF to a file
output_file = open('output.pdf', 'wb')
pdf_writer.write(output_file)

# Close the files
pdf_file.close()
output_file.close()

