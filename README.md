# Agentic AI Discharge Summary System

> AI-powered healthcare application that automatically generates clinician-review discharge summary drafts from multiple patient PDF records.

---

## Overview

Unlike traditional PDF summarization systems, this project follows an **agentic workflow** that can:

- Extract clinical information from multiple PDFs
- Perform OCR on scanned documents
- Identify diagnoses and medications
- Detect missing information
- Reconcile medications
- Detect conflicts
- Identify pending results
- Perform safety validation
- Generate an auditable reasoning trace
- Produce structured discharge summaries

---

## Problem Statement

Preparing discharge summaries manually requires reviewing multiple clinical notes, laboratory reports, medication charts, and discharge instructions. This process is time-consuming and prone to documentation errors.

The Agentic AI Discharge Summary System assists healthcare professionals by generating a structured discharge summary draft while maintaining **transparency and clinician oversight**.

---

## Features

### 📄 PDF Processing
- Upload multiple patient PDFs
- Extract text from all pages
- OCR support for scanned documents using Tesseract
- Error handling for extraction failures

### 🤖 Agent-Based Workflow
- Planner-based reasoning
- Missing information detection
- Clinical information extraction
- Medication extraction
- Pending result detection
- Conflict detection

### 💊 Medication Reconciliation

Compare admission vs. discharge medications and identify:

| Change Type | Description |
|-------------|-------------|
| Added | Medications newly prescribed at discharge |
| Removed | Medications discontinued at discharge |
| Changed | Medications with modified dosage or instructions |

### 🛡️ Safety Validation

Detect:
- Missing diagnosis
- Missing dates
- Missing allergy information
- Medication conflicts
- Drug interaction warnings

### 📦 Output Generation
- `summary.json`
- `trace.json`
- `discharge_summary.txt`

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| Backend | Python |
| AI Model | Google Gemini API |
| PDF Processing | PyMuPDF, Tesseract OCR |
| Data Validation | Pydantic |
| Data Processing | Pandas |

---

## Project Structure

```
Agentic-AI-Discharge-Summary-System/
│
├── app.py
│
├── agents/
│   ├── planner.py
│   ├── extractor.py
│   ├── reconciliation.py
│   ├── validator.py
│   └── summary_generator.py
│
├── tools/
│   ├── pdf_reader.py
│   ├── document_search.py
│   ├── conflict_detector.py
│   ├── drug_checker.py
│   └── escalation.py
│
├── models/
│   └── schemas.py
│
├── utils/
│   └── json_parser.py
│
├── outputs/
│
├── requirements.txt
│
└── README.md
```

---

## Agent Workflow

```
Upload PDFs
      │
      ▼
PDF Reader Tool
      │
      ▼
OCR Processing
      │
      ▼
Agent Planner
      │
      ▼
Clinical Extractors
 ├─ Diagnosis Extractor
 ├─ Medication Extractor
 ├─ Clinical Extractor
 └─ Pending Result Extractor
      │
      ▼
Medication Reconciliation
      │
      ▼
Conflict Detection
      │
      ▼
Safety Validation
      │
      ▼
Discharge Summary Generation
      │
      ▼
Download Outputs
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/Agentic-AI-Discharge-Summary-System.git
cd Agentic-AI-Discharge-Summary-System
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / Mac:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Outputs

| File | Description |
|------|-------------|
| `summary.json` | Structured clinical information extracted from documents |
| `trace.json` | Agent reasoning trace (step, tool used, input, output, next decision) |
| `discharge_summary.txt` | Clinician-review discharge summary draft |

### Sample Output

```
PRINCIPAL DIAGNOSIS
ACUTE GASTROENTERITIS WITH DEHYDRATION

SECONDARY DIAGNOSIS
URINARY TRACT INFECTION

ALLERGIES
No Known Drug Allergies

PENDING RESULTS
Urine Culture and Sensitivity
```

---

## Future Enhancements

- [ ] True iterative ReAct agent loop
- [ ] Page-level evidence citations
- [ ] Confidence scoring
- [ ] Advanced conflict reconciliation
- [ ] Clinician escalation workflow
- [ ] Follow-up instruction extraction
- [ ] Drug interaction knowledge base integration

---

## ⚠️ Disclaimer

This system generates **AI-assisted discharge summary drafts for clinician review**.

> **AI Generated Draft. Requires Clinician Review. Do Not Use As Final Clinical Documentation.**

---

## Author

**Niranjan NN**  
AI Engineer | Data Science | Full Stack Development

*Built as part of an Agentic AI Healthcare Automation Project.*
