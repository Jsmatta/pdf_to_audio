from setuptools import setup, find_packages

setup(
    name="pdftts",  # Name of your tool
    version="1.0.0",
    author="Jaiveer Matta",
    description="Convert PDF files to audio using text-to-speech",
    packages=find_packages(),
    install_requires=[
        "PyPDF2",
        "gtts",
        "pyttsx3",
    ],
    entry_points={
        "console_scripts": [
            "pdftts=main:main",  # Command-line tool name and entry point
        ],
    },
)