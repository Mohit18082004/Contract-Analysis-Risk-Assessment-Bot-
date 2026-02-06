import spacy
import nltk
from nltk.tokenize import sent_tokenize
import re
from typing import List

class NLPProcessor:
    def __init__(self):
        # Load spaCy model
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except:
            # Download if not available
            import subprocess
            subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
            self.nlp = spacy.load("en_core_web_sm")
        
        # Download NLTK data
        nltk.download('punkt', quiet=True)
    
    def extract_clauses(self, contract_text: str) -> List[str]:
        """Extract individual clauses from contract text"""
        # Split by common clause indicators
        clause_patterns = [
            r'\n\d+\.\s',  # 1. Clause
            r'\n\([a-z]\)\s',  # (a) Sub-clause
            r'\nSECTION\s+\d+',  # SECTION 1
            r'\nARTICLE\s+\d+',  # ARTICLE I
            r'\n\d+\.\d+\.',  # 1.1. Numbering
        ]
        
        # First, try splitting by patterns
        for pattern in clause_patterns:
            clauses = re.split(pattern, contract_text)
            if len(clauses) > 1:
                # Clean up clauses
                cleaned_clauses = []
                for clause in clauses:
                    clause = clause.strip()
                    if len(clause) > 50:  # Minimum clause length
                        cleaned_clauses.append(clause)
                if len(cleaned_clauses) > 3:
                    return cleaned_clauses
        
        # Fallback: split by sentences and group
        sentences = sent_tokenize(contract_text)
        clauses = []
        current_clause = []
        
        for sentence in sentences:
            current_clause.append(sentence)
            if len(current_clause) >= 3 or sentence.endswith((':', ';')):
                clauses.append(' '.join(current_clause))
                current_clause = []
        
        if current_clause:
            clauses.append(' '.join(current_clause))
        
        return clauses
    
    def extract_entities(self, text: str):
        """Extract named entities using spaCy"""
        doc = self.nlp(text)
        entities = {
            "PARTIES": [],
            "DATES": [],
            "AMOUNTS": [],
            "ORGANIZATIONS": [],
            "LAWS": []
        }
        
        for ent in doc.ents:
            if ent.label_ in ["PERSON", "ORG"]:
                entities["PARTIES"].append(ent.text)
            elif ent.label_ == "DATE":
                entities["DATES"].append(ent.text)
            elif ent.label_ == "MONEY":
                entities["AMOUNTS"].append(ent.text)
            elif ent.label_ == "LAW":
                entities["LAWS"].append(ent.text)
        
        return entities