import pyttsx3
import PyPDF2
from tkinter import filedialog
from tkinter import Tk

# Initialize Tkinter
root = Tk()
root.withdraw()

# Ask user to select a PDF file
book = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

# Check if the file is selected
if book:
    try:
        # Open the PDF file
        with open(book, "rb") as file:
            pdfreader = PyPDF2.PdfReader(file)
            pages = len(pdfreader.pages)

            # Iterate through each page and extract text
            for num in range(pages):
                page = pdfreader.pages[num]
                text = page.extract_text()

                # Initialize the text-to-speech engine
                player = pyttsx3.init()

                # Say the extracted text
                player.say(text)
                player.runAndWait()
    except PyPDF2.utils.PdfReadError as e:
        print("Error reading the PDF file:", e)
        print("The PDF file may be corrupted or have an incorrect structure.")
else:
    print("No file selected.")
