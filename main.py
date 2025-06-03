import pyttsx3
import PyPDF2
import sys

if len(sys.argv) > 1:
    book = sys.argv[1]
    
# Function to read a PDF file and return its text content
def read_pdf(file_path):
    try:
        text = "" # empty string with no content
        with open(file_path, 'rb') as file: # open file 
            reader = PyPDF2.PdfReader(file) # read the pdf file
            if len(reader.pages) == 0:
                return None
            
            for page in reader.pages: # go tyhrough all the pages
                page_text = page.extract_text() # get the text
                if page_text:
                    text += page_text + "\n" # add a new line after each page's text
        
        return text.strip() if text.strip() else None # none returned if no text
    
    #error if no file is found or the pdf can't be read
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

# text to speech function
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
# main execution
if __name__ == "__main__":
    reaed_text = read_pdf(book)
    if reaed_text:
        speak(reaed_text)
    else:
        speak("The PDF file is empty or could not be read.")
    
    