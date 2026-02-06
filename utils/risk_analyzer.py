import re
import json
from typing import Dict, List, Tuple
import os

try:
    from openai import OpenAI
    HAS_OPENAI = True
except (ImportError, ModuleNotFoundError):
    HAS_OPENAI = False
    OpenAI = None

class RiskAnalyzer:
    def __init__(self):
        # Initialize OpenAI client if available
        if HAS_OPENAI:
            api_key = os.environ.get("OPENAI_API_KEY")
            if api_key:
                self.client = OpenAI(api_key=api_key)
            else:
                self.client = None
        else:
            self.client = None
        
        # Define risk patterns (can be expanded)
        self.risk_patterns = {
            "high_risk": [
                r"unilateral termination",
                r"exclusive jurisdiction",
                r"indemnify.*all losses",
                r"perpetual license",
                r"irrevocable.*right",
                r"automatic renewal",
                r"liquidated damages.*excessive",
                r"without cause"
            ],
            "medium_risk": [
                r"confidentiality.*indefinite",
                r"non-compete.*2 years",
                r"arbitration.*company.*venue",
                r"force majeure.*broad"
            ],
            "low_risk": [
                r"mutual agreement",
                r"reasonable.*notice",
                r"good faith",
                r"pro rata"
            ]
        }
        
        # Keywords for different risk categories
        self.risk_categories = {
            "Penalty Clauses": ["penalty", "liquidated damages", "fine", "forfeit"],
            "Indemnity": ["indemnify", "hold harmless", "defend"],
            "Termination": ["terminate", "cancel", "expire", "renewal"],
            "Jurisdiction": ["jurisdiction", "venue", "governing law"],
            "IP Rights": ["intellectual property", "copyright", "patent", "trade secret"],
            "Confidentiality": ["confidential", "non-disclosure", "proprietary"]
        }
    
    def assess_clause_risk(self, clause_text: str) -> str:
        """Assess risk level of a clause"""
        clause_lower = clause_text.lower()
        
        # Check for high risk patterns
        for pattern in self.risk_patterns["high_risk"]:
            if re.search(pattern, clause_lower, re.IGNORECASE):
                return "High"
        
        # Check for medium risk patterns
        for pattern in self.risk_patterns["medium_risk"]:
            if re.search(pattern, clause_lower, re.IGNORECASE):
                return "Medium"
        
        return "Low"
    
    def get_risk_category(self, clause_text: str) -> str:
        """Categorize the risk"""
        clause_lower = clause_text.lower()
        for category, keywords in self.risk_categories.items():
            for keyword in keywords:
                if keyword in clause_lower:
                    return category
        return "General"
    
    def calculate_overall_risk(self, results: List[Dict]) -> str:
        """Calculate overall contract risk"""
        risk_scores = {"High": 3, "Medium": 2, "Low": 1}
        total_score = 0
        
        for result in results:
            total_score += risk_scores.get(result["Risk Level"], 1)
        
        avg_score = total_score / len(results) if results else 1
        
        if avg_score >= 2.5:
            return "High Risk"
        elif avg_score >= 1.5:
            return "Medium Risk"
        else:
            return "Low Risk"
    
    def explain_clause(self, clause_text: str) -> str:
        """Generate plain language explanation using GPT-4"""
        if not HAS_OPENAI or not self.client:
            return "⚠️ OpenAI API not configured. Set OPENAI_API_KEY environment variable to enable AI explanations."
        
        prompt = f"""
        Explain this legal clause in simple business English:
        
        "{clause_text}"
        
        Explain in 2-3 sentences what this means for a business owner.
        Focus on obligations, rights, and practical implications.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=150
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            error_name = type(e).__name__
            if "AuthenticationError" in error_name:
                return "⚠️ OpenAI authentication failed. Check your OPENAI_API_KEY is valid."
            elif "RateLimitError" in error_name:
                return "⚠️ OpenAI rate limit exceeded. Please try again later."
            else:
                return f"⚠️ Unable to generate explanation: {error_name}"
    
    def suggest_alternative(self, clause_text: str) -> str:
        """Suggest alternative wording for risky clauses"""
        if not HAS_OPENAI or not self.client:
            return "⚠️ OpenAI API not configured. Set OPENAI_API_KEY environment variable to enable suggestions."
        
        prompt = f"""
        This is a potentially risky contract clause:
        
        "{clause_text}"
        
        Suggest a more balanced alternative that protects both parties.
        Provide 1-2 alternative phrasings in plain English.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=200
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            error_name = type(e).__name__
            if "AuthenticationError" in error_name:
                return "⚠️ OpenAI authentication failed. Check your OPENAI_API_KEY is valid."
            elif "RateLimitError" in error_name:
                return "⚠️ OpenAI rate limit exceeded. Please try again later."
            else:
                return f"⚠️ Suggestions unavailable: {error_name}"