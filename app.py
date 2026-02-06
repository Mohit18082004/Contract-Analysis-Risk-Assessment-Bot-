import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os
from openai import OpenAI
from utils.document_parser import DocumentParser
from utils.nlp_processor import NLPProcessor
from utils.risk_analyzer import RiskAnalyzer

load_dotenv()  # loads .env if present

# Read OpenAI API key from environment or .env (do NOT hard-code secret keys here)

key = os.getenv("OPENAI_API_KEY")
print("Key present:", bool(key))
if not key:
    print("OPENAI_API_KEY not set")
else:
    try:
        client = OpenAI(api_key=key)
        models = client.models.list()
        print("OpenAI reachable, models count:", len(models.data))
    except Exception as e:
        print("OpenAI error:", type(e).__name__, e)

# Page config
st.set_page_config(
    page_title="Legal Contract Assistant",
    page_icon="⚖️",
    layout="wide"
)

# Initialize session state
if 'contract_text' not in st.session_state:
    st.session_state.contract_text = ""
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None

# Sidebar
with st.sidebar:
    st.title("⚖️ Legal Contract AI")
    st.markdown("---")
    
    # File upload
    uploaded_file = st.file_uploader(
        "Upload Contract",
        type=['pdf', 'docx', 'txt'],
        help="Supported formats: PDF, DOCX, TXT"
    )
    
    # Contract type selection
    contract_type = st.selectbox(
        "Contract Type",
        ["Auto-detect", "Employment", "Vendor", "Lease", "Partnership", "Service"]
    )
    
    # Language selection
    language = st.radio("Contract Language", ["English", "Hindi"])
    
    analyze_button = st.button("🔍 Analyze Contract", type="primary")

# Main area
st.title("📄 GenAI Legal Contract Assistant")
st.markdown("---")

if uploaded_file:
    # Parse document
    parser = DocumentParser()
    contract_text = parser.parse_file(uploaded_file, language)
    st.session_state.contract_text = contract_text
    
    # Display preview
    with st.expander("📋 Contract Preview"):
        st.text_area("Extracted Text", contract_text[:2000], height=200)

if analyze_button and st.session_state.contract_text:
    with st.spinner("Analyzing contract..."):
        # Initialize processors
        nlp = NLPProcessor()
        analyzer = RiskAnalyzer()
        
        # Extract clauses
        clauses = nlp.extract_clauses(st.session_state.contract_text)
        
        # Analyze each clause
        results = []
        for i, clause in enumerate(clauses):
            risk_score = analyzer.assess_clause_risk(clause)
            explanation = analyzer.explain_clause(clause)
            suggestion = analyzer.suggest_alternative(clause)
            
            results.append({
                "Clause #": i+1,
                "Text": clause[:100] + "...",
                "Risk Level": risk_score,
                "Risk Category": analyzer.get_risk_category(clause),
                "Explanation": explanation,
                "Suggestion": suggestion
            })
        
        st.session_state.analysis_results = results
        
        # Display results
        st.subheader("📊 Risk Analysis Summary")
        
        # Overall risk score
        overall_risk = analyzer.calculate_overall_risk(results)
        st.metric("Overall Risk Score", overall_risk)
        
        # Risk breakdown
        col1, col2, col3 = st.columns(3)
        with col1:
            high_risk = len([r for r in results if r["Risk Level"] == "High"])
            st.metric("High Risk Clauses", high_risk, delta_color="inverse")
        with col2:
            medium_risk = len([r for r in results if r["Risk Level"] == "Medium"])
            st.metric("Medium Risk Clauses", medium_risk)
        with col3:
            low_risk = len([r for r in results if r["Risk Level"] == "Low"])
            st.metric("Low Risk Clauses", low_risk)
        
        # Detailed analysis
        st.subheader("🔍 Clause-by-Clause Analysis")
        for result in results:
            with st.expander(f"Clause {result['Clause #']} - {result['Risk Level']} Risk"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Original Text:**")
                    st.info(result['Text'])
                    st.markdown(f"**Risk Category:** {result['Risk Category']}")
                with col2:
                    st.markdown(f"**Plain Language Explanation:**")
                    st.success(result['Explanation'])
                    st.markdown(f"**Suggested Alternative:**")
                    st.warning(result['Suggestion'])
        
        # Export options
        st.subheader("📤 Export Options")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📄 Generate PDF Report"):
                # Generate PDF logic
                st.success("PDF generated successfully!")
        with col2:
            if st.button("📊 Export to CSV"):
                df = pd.DataFrame(results)
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name="contract_analysis.csv"
                )
        with col3:
            if st.button("⚖️ Generate Template"):
                st.info("Standard template generated")

# streamlit run c:/Users/mm091/Downloads/contract-ai-assistant/app.py [ARGUMENTS] & .venv/Scripts/python.exe -m streamlit run app.py