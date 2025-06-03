# PDF to Audio

This program turns the text in a pdf file to audio.

It takes arguments in the terminal to determine what happens to the files.

## Arguments:
``` shell
    document.pdf                    # Play audio directly
    document.pdf -a                 # Play audio (explicit)
    document.pdf -s                 # Save as MP3
    document.pdf -s -o my_book.mp3  # Save with custom name
    document.pdf -r 150 -v 0.8      # Custom rate and volume
```

The program utilizes the libraries:
- [pyttsx3](https://pypi.org/project/pyttsx3/) For the text to speech
- [PyPDF2](https://pypi.org/project/PyPDF2/) To read the contents of the pdf file.
- [pathlib](https://docs.python.org/3/library/pathlib.html) to Handle the file paths 