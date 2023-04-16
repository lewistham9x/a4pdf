import os
import PyPDF2
from pdf2image import convert_from_path
from PIL import Image

import cairosvg


def convert_svg_to_pdf(input_path, output_path):
    try:
        cairosvg.svg2pdf(url=input_path, write_to=output_path)
        return True
    except Exception as e:
        print(f"Error converting {input_path} to PDF: {e}")
        return False


# Function to rotate and scale down the PDF pages
def process_pdf(file_path, output_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        writer = PyPDF2.PdfFileWriter()

        for page_num in range(reader.getNumPages()):
            page = reader.getPage(page_num)

            # Determine if the page should be rotated
            if page.mediaBox[2] < page.mediaBox[3]:
                page.rotateClockwise(90)

            # Scale down to A4 height (297 mm) while maintaining aspect ratio
            width, height = page.mediaBox[2], page.mediaBox[3]
            new_height = int(297 * 72 / 25.4)  # Convert to points (72 points/inch)
            scale_factor = new_height / float(height)
            new_width = float(width) * scale_factor

            page.scaleTo(new_width, new_height)

            # Add the processed page to the output PDF
            writer.addPage(page)

        # Save the output PDF
        with open(output_path, "wb") as output_file:
            writer.write(output_file)


def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name + ".pdf")

        # Convert SVG to PDF before processing
        if file_name.lower().endswith(".svg"):
            temp_pdf_path = os.path.join(output_folder, file_name[:-4] + ".pdf")
            if convert_svg_to_pdf(input_path, temp_pdf_path):
                process_pdf(temp_pdf_path, output_path)
                os.remove(temp_pdf_path)  # Remove temporary PDF file
                print(f"Processed {input_path} -> {output_path}")
        elif file_name.lower().endswith(".pdf"):
            process_pdf(input_path, output_path)
            print(f"Processed {input_path} -> {output_path}")


# Set your input and output folder paths
input_folder = "/Users/lewistham/Downloads/proj/out/operator diags/final"
output_folder = "output_pdfs"

# Process all PDFs in the input folder
process_folder(input_folder, output_folder)
