# A4 PDF

This Python script is designed to process PDF files within a specified input folder and output the processed PDF files to a specified output folder. The script uses the PyPDF2 and pdf2image libraries to rotate and scale down the pages of the input PDF files while maintaining the aspect ratio of the pages. The output PDF files are saved to the output folder.

## Installation

To use this script, you will need to install the PyPDF2, pdf2image, and PIL (Python Imaging Library) libraries in your Python environment. You can do this using pip, the Python package manager, by running the following command in your terminal or command prompt:

```
pip install PyPDF2 pdf2image Pillow
```

## Usage

Once you have installed the required libraries, you can run the script by setting the `input_folder` and `output_folder` variables to the paths of your input and output folders, respectively. Then, run the script using a Python interpreter.

Note that the script assumes that all PDF files within the input folder have a `.pdf` extension. Any files in the input folder that do not have this extension will not be processed.

After running the script, you will see a message for each PDF file that has been processed, indicating the path of the input file and the path of the output file.
