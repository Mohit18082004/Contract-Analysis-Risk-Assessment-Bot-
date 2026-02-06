# Contract AI Assistant - Project Structure

## Overview
This project is a contract analysis and generation tool using AI and NLP techniques to process legal documents.

## Directory Structure

```
contract-ai-assistant/
│
├── app.py                           # Main Streamlit application entry point
├── requirements.txt                 # Python dependencies
│
├── models/                          # Machine learning models directory
│   ├── ner_model/                   # Named Entity Recognition model for legal terms
│   │   ├── meta.json                # NER model metadata and configuration
│   │   ├── config.cfg               # SpaCy NER model configuration
│   │   ├── ner_model/               # Trained model directory
│   │   │   ├── model                # Compiled NER model
│   │   │   └── vocab/               # Vocabulary and word embeddings
│   │   └── training_data.json       # Training dataset for NER
│   │
│   ├── classifiers/                 # Contract type classification models
│   │   ├── contract_classifier.pkl  # Main contract type classifier (pickled)
│   │   ├── risk_classifier.pkl      # Risk level classification model
│   │   └── feature_extractor.pkl    # Feature extraction pipeline
│   │
│   └── embeddings/                  # Pre-trained word embeddings
│       ├── legal_embeddings.npy     # Legal domain word embeddings
│       └── word_index.json          # Word to embedding index mapping
│
├── templates/                       # Contract template files
│   ├── employment_agreement.txt      # Employment agreement template
│   ├── vendor_contract.txt           # Vendor contract template
│   ├── lease_agreement.txt           # Lease agreement template
│   ├── partnership_deed.txt          # Partnership deed template
│   ├── service_contract.txt          # Service contract template
│   ├── nda_agreement.txt             # Non-Disclosure Agreement template
│   ├── consultancy_agreement.txt     # Consultancy agreement template
│   └── sales_agreement.txt           # Sales agreement template
│
├── data/                            # Data files and resources
│   ├── audit_logs.json              # System audit and activity logs
│   └── risk_keywords.json           # Keywords for risk detection
│
├── utils/                           # Utility modules
│   ├── document_parser.py           # PDF/document parsing functionality
│   ├── risk_analyzer.py             # Contract risk analysis logic
│   ├── nlp_processor.py             # NLP and text processing utilities
│   └── template_generator.py        # Contract template generation
│
└── PROJECT_STRUCTURE.md             # This file - project structure reference
```

## Module Descriptions

### Utility Modules
| Module | Purpose |
|--------|---------|
| `app.py` | Main Streamlit web application interface |
| `document_parser.py` | Handles parsing and extraction from contract documents |
| `risk_analyzer.py` | Analyzes contracts for potential risks and red flags |
| `nlp_processor.py` | Performs NLP tasks including tokenization, NER, and text processing |
| `template_generator.py` | Generates contract templates based on user input |

### ML Models
| Component | Purpose |
|-----------|---------|
| `ner_model/` | Named Entity Recognition model for extracting legal terms, parties, and entities |
| `ner_model/meta.json` | Metadata about the NER model (version, performance metrics) |
| `ner_model/config.cfg` | SpaCy configuration for NER model training |
| `ner_model/ner_model/model` | Compiled, trained NER model |
| `ner_model/training_data.json` | Annotated training dataset for NER |
| `classifiers/contract_classifier.pkl` | Identifies contract types (employment, vendor, lease, etc.) |
| `classifiers/risk_classifier.pkl` | Classifies risk level (low, medium, high) |
| `classifiers/feature_extractor.pkl` | Extracts features for classification tasks |
| `embeddings/legal_embeddings.npy` | Pre-trained word embeddings for legal domain |
| `embeddings/word_index.json` | Mapping of words to embedding indices |

### Data Files
| File | Purpose |
|------|---------|
| `audit_logs.json` | Tracks user actions, model predictions, and system events |
| `risk_keywords.json` | Keywords dictionary for risk detection and flagging |

### Templates
| Template | Use Case |
|----------|----------|
| `employment_agreement.txt` | Employee hiring and employment contracts |
| `vendor_contract.txt` | Vendor/supplier agreements |
| `lease_agreement.txt` | Property lease agreements |
| `partnership_deed.txt` | Partnership formation documents |
| `service_contract.txt` | Service provision contracts |
| `nda_agreement.txt` | Non-Disclosure Agreement |
| `consultancy_agreement.txt` | Consultant engagement contracts |
| `sales_agreement.txt` | Product/service sales agreements |

## Quick Start

1. Install dependencies: `pip install -r requirements.txt`
2. Run the application: `streamlit run app.py`
3. Access the web interface at `http://localhost:8501`

## Notes

- Ensure all model files are properly trained and saved in `models/` directory
- Update `risk_keywords.json` with domain-specific terminology as needed
- Templates in `templates/` can be customized for different contract types
