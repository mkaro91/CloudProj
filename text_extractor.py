import PyPDF2
import docx

def extract_text(filepath, file_extension):
        
    file_extension = file_extension.lower()

    # Extract text from .txt files
    if file_extension == 'txt':
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    
    # Extract text from .pdf files
    elif file_extension == 'pdf':
        text = ""
        with open(filepath, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text   
        return text

    # Extract text from word document files (.docx)
    elif file_extension == 'docx':
        doc = docx.Document(filepath)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    
    # In case the file is an unsupported type
    else:
        raise ValueError("Unsupported file type")