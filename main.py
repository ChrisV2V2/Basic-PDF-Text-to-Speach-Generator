import pyttsx3
import PyPDF2
from tkinter import filedialog
from tkinter import Tk

engine = pyttsx3.init() # object creation
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # Set voices[0] for a male voice.

# Create a Tkinter root window
root = Tk()
root.withdraw()  # Hide the Tkinter root window

# Ask the user to select a PDF file
fileName = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

# Open the selected PDF file in read-binary mode
with open(fileName, 'rb') as file:
    pdfReader = PyPDF2.PdfReader(file)
    num_pages = len(pdfReader.pages)  # Get the number of pages in the PDF

    # Iterate through each page and extract text
    for page_num in range(num_pages):
        page = pdfReader.pages[page_num]
        text = page.extract_text()

        # Initialise pyttsx3 engine to convert text to speech
        player = pyttsx3.init()
        player.say(text)
        player.runAndWait()
