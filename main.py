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
    parser = argparse.ArgumentParser(
        description="Convert PDF files to audio using text-to-speech",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
    Examples:
    %(prog)s document.pdf                    # Play audio directly
    %(prog)s document.pdf -a                 # Play audio (explicit)
    %(prog)s document.pdf -s                 # Save as MP3
    %(prog)s document.pdf -s -o my_book.mp3  # Save with custom name
    %(prog)s document.pdf -r 150 -v 0.8      # Custom rate and volume
        """
    )
        # arguments for the command line
    parser.add_argument('pdf_file', 
                        help='Path to the PDF file to convert')

    parser.add_argument('-a', '--audio', 
                        action='store_true',
                        help='Play the audio directly (default behavior)')

    parser.add_argument('-s', '--save', 
                        action='store_true',
                        help='Save the audio as an MP3 file')

    parser.add_argument('-o', '--output', 
                        type=str,
                        help='Output filename for saved audio (used with -s)')

    parser.add_argument('-r', '--rate', 
                        type=int, 
                        default=200,
                        help='Speech rate (words per minute, default: 200)')

    parser.add_argument('-v', '--volume', 
                        type=float, 
                        default=0.9,
                        help='Volume level (0.0 to 1.0, default: 0.9)')

    parser.add_argument('--preview', 
                        action='store_true',
                        help='Show first 500 characters of extracted text')

    args = parser.parse_args()

    # Validate PDF file exists
    if not os.path.isfile(args.pdf_file):
        print(f"Error: PDF file '{args.pdf_file}' does not exist.")
        sys.exit(1)

    # Validate volume range
    if not 0.0 <= args.volume <= 1.0:
        print("Error: Volume must be between 0.0 and 1.0")
        sys.exit(1)

    # Read PDF content
    print(f"Reading PDF: {args.pdf_file}")
    text = read_pdf(args.pdf_file)

    if not text:
        print("Error: The PDF file is empty or could not be read.")
        sys.exit(1)

    print(f"Successfully extracted {len(text)} characters from PDF.")

    # Show preview if requested
    if args.preview:
        preview_text = text[:500] + "..." if len(text) > 500 else text
        print(f"\nPreview of extracted text:\n{'-'*50}")
        print(preview_text)
        print(f"{'-'*50}\n")

    # Default behavior: play audio if no specific action is specified
    if not args.save:
        args.audio = True

    # Save audio to file
    if args.save:
        output_file = get_output_filename(args.pdf_file, args.output)
        save_audio(text, output_file, args.rate, args.volume)

    # Play audio
    if args.audio:
        speak_text(text, args.rate, args.volume)

# main execution
if __name__ == "__main__":
    main()