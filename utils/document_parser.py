import PyPDF2
from docx import Document

try:
    from deep_translator import GoogleTranslator
    HAS_TRANSLATOR = True
except (ImportError, ModuleNotFoundError):
    HAS_TRANSLATOR = False
    GoogleTranslator = None

class DocumentParser:
    def __init__(self):
        self.translator = GoogleTranslator(source='hi', target='en') if HAS_TRANSLATOR else None
    
    def parse_file(self, file, language="English"):
        """Parse uploaded file and extract text"""
        text = ""
        
        if file.name.endswith('.pdf'):
            text = self._parse_pdf(file)
        elif file.name.endswith('.docx'):
            text = self._parse_docx(file)
        elif file.name.endswith('.txt'):
            text = file.read().decode('utf-8')
        
        # Translate if Hindi
        if language == "Hindi":
            text = self._translate_hindi_to_english(text)
        
        return text
    
    def _parse_pdf(self, file):
        """Extract text from PDF"""
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    
    def _parse_docx(self, file):
        """Extract text from DOCX"""
        doc = Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    
    def _translate_hindi_to_english(self, text):
        """Translate Hindi text to English"""
        if not HAS_TRANSLATOR or self.translator is None:
            return text  # Return original if translator is not available
        
        try:
            # Translate in chunks if text is long
            if len(text) > 4000:
                chunks = [text[i:i+4000] for i in range(0, len(text), 4000)]
                translated_chunks = []
                for chunk in chunks:
                    translated_text = self.translator.translate(chunk)
                    translated_chunks.append(translated_text)
                return " ".join(translated_chunks)
            else:
                translated_text = self.translator.translate(text)
                return translated_text
        except:
            return text  # Return original if translation fails