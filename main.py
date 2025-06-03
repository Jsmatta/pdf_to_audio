import pyttsx3
import PyPDF2
import argparse # to handle command line arguments
import sys
import os
from pathlib import Path # to handle file paths

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
def speak_text(text, rate=200, volume=0.9):
    try:
        engine = pyttsx3.init() # initialize the text to speech engine
        
        # Set speech rate and volume
        engine.setProperty('rate', rate) # speech speed 
        engine.setProperty('volume', volume) # speech volume
        
        print("Playing audio...") # print message to console
        engine.say(text)
        
        # wait for the audio to finish
        engine.runAndWait() 
        print("Audio playback completed.")
    #error message if text is not playable
    except Exception as e:
        print(f"Error during speech synthesis: {e}")

#Save the text to an audio file
def save_audio(text, output_path, rate=200, volume=0.9):

    try:
        engine = pyttsx3.init()
        
        # Set speech rate and volume
        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        
        print(f"Saving audio to '{output_path}'...") # print message to console
        engine.save_to_file(text, output_path)
        engine.runAndWait()
        print(f"Audio saved successfully to '{output_path}'") 
        
    except Exception as e:
        print(f"Error saving audio: {e}")

#create output file name
def get_output_filename(pdf_path, custom_name=None):
    if custom_name: # if a custom name is provided
        if not custom_name.endswith(('.mp3', '.wav')):
            custom_name += '.mp3'
        return custom_name
    
    pdf_name = Path(pdf_path).stem # get name of the pdf file
    return f"{pdf_name}_audio.mp3"


def main():
    return

# main execution
if __name__ == "__main__":
    main()