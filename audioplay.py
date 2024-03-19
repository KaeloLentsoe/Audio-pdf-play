import pyttsx3
import PyPDF2
from tkinter import filedialog
from tkinter import Tk


root = Tk()
root.withdraw()

book = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])


if book:
    try:
       
        with open(book, "rb") as file:
            pdfreader = PyPDF2.PdfReader(file)
            pages = len(pdfreader.pages)

            
            for num in range(pages):
                page = pdfreader.pages[num]
                text = page.extract_text()

               
                player = pyttsx3.init()

              
                player.say(text)
                player.runAndWait()
    except PyPDF2.utils.PdfReadError as e:
        print("Error reading the PDF file:", e)
        print("The PDF file may be corrupted or have an incorrect structure.")
else:
    print("No file selected.")
