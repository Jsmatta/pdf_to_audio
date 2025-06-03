import pyttsx3
import PyPDF2
import sys

if len(sys.argv) > 1:
    book = sys.argv[1]
# Function to read a PDF file and return its text content

def read_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text # returns the text from the pdf file

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
if __name__ == "__main__":
    reaed_text = read_pdf(book)
    if reaed_text:
        speak(reaed_text)
    else:
        speak("The PDF file is empty or could not be read.")
    # speak("Hello, this is a text-to-speech test.")
    # speak("How can I assist you today?")
    # speak("Goodbye!")
    
    