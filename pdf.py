import os
import PyPDF2
from pdf2image import convert_from_path
from PIL import Image


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
            aspect_ratio = int(width / height)
            new_height = int(297 * 72 / 25.4)  # Convert to points (72 points/inch)
            new_width = new_height * aspect_ratio

            page.scaleTo(new_width, new_height)

            # Add the processed page to the output PDF
            writer.addPage(page)

        # Save the output PDF
        with open(output_path, "wb") as output_file:
            writer.write(output_file)


# Main function to process all PDFs in a folder
def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(".pdf"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            process_pdf(input_path, output_path)
            print(f"Processed {input_path} -> {output_path}")


# Set your input and output folder paths
input_folder = "input_pdfs"
output_folder = "output_pdfs"

# Process all PDFs in the input folder
process_folder(input_folder, output_folder)
