## Audio PDF Reader

### Purpose:
The Python script provided serves the purpose of creating an audio PDF reader. It allows users to select a PDF file and then reads aloud the content of each page using text-to-speech (TTS) technology.

### Libraries Used:
1. **PyPDF2**: This library is used to extract text from PDF files. It provides functionalities to work with PDF documents in Python.
2. **pyttsx3**: This library is used for text-to-speech conversion. It provides an interface to various TTS engines in Python.

### Installation:
Before running the script, ensure that you have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/downloads/)

#### Dependencies:
- **PyPDF2**: Run the following command to install PyPDF2:
  ```
  pip install PyPDF2
  ```

- **pyttsx3**: Run the following command to install pyttsx3:
  ```
  pip install pyttsx3
  ```

### Usage:
1. **Setup**: Ensure that Python is installed on your system and install the required libraries using the provided commands.
2. **Execution**: Run the script, and it will display a file dialog for selecting a PDF file.
3. **Interaction**: After selecting a PDF file, the script will start reading its content aloud.
4. **Customization**: Users can customize the voice, speech rate, and other settings using pyttsx3's configuration options within the script.

### Note:
If you encounter any errors or issues during execution, please refer to the error messages displayed by the script. It provides information about potential problems such as a corrupted PDF file.

### Example:
```bash
python audio_pdf_reader.py
```

--- 

To install the required dependencies use `pip`. Users can follow these instructions to set up the project environment before running the script.