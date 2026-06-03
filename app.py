import os
import json
import streamlit as st
from google import genai

from dotenv import load_dotenv
from utils.json_parser import parse_llm_json
from tools.pdf_reader import PDFReaderTool
from tools.document_search import DocumentSearchTool
from tools.drug_checker import DrugInteractionTool
from tools.escalation import ClinicianEscalationTool
from tools.conflict_detector import (
    ConflictDetectorTool
)
from agents.extractor import (
    DiagnosisExtractorTool,
    MedicationExtractorTool,
    PendingResultTool,
    ClinicalExtractorTool
)

from agents.planner import AgentPlanner
from agents.reconciliation import MedicationReconciliation
from agents.validator import SafetyValidator
from agents.summary_generator import SummaryGenerator

from models.schemas import DischargeSummary

load_dotenv()

from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.title("Agentic AI Discharge Summary System")

uploaded_files = st.file_uploader(
    "Upload Patient PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    documents = []

    for file in uploaded_files:
        docs = PDFReaderTool.extract(file)
        documents.extend(docs)

    st.subheader("Extracted Text")

    combined_text = ""

    for d in documents:
        if "text" in d:
            combined_text += d["text"]
            st.write(
                "Total Characters Extracted:",
                len(combined_text)
            )

    if st.button("Run Agent"):

        planner = AgentPlanner()

        summary = DischargeSummary()

        diagnosis_tool = DiagnosisExtractorTool(client)
        medication_tool = MedicationExtractorTool(client)
        pending_tool = PendingResultTool(client)
        clinical_tool = ClinicalExtractorTool(client)

        MAX_ITERATIONS = 10

        for step in range(MAX_ITERATIONS):

            planner.add_trace(
                step,
                "Evaluate missing fields",
                "Planner",
                "Current Summary",
                "Checked",
                "Continue"
            )

            if not summary.principal_diagnosis:

                diag_raw = diagnosis_tool.run(combined_text)

                planner.add_trace(
                    step,
                    "Need diagnosis",
                    "DiagnosisExtractorTool",
                    "Patient Notes",
                    diag_raw,
                    "Update Summary"
                )

                diag = parse_llm_json(diag_raw)

                summary.principal_diagnosis = diag.get(
                    "principal",
                    "Missing – Requires Clinician Review"
                )

                summary.secondary_diagnoses = diag.get(
                    "secondary",
                    []
                )

            if not summary.discharge_medications:

                meds_raw = medication_tool.run(combined_text)

                planner.add_trace(
                    step,
                    "Need medications",
                    "MedicationExtractorTool",
                    "Patient Notes",
                    meds_raw,
                    "Reconcile"
                )

                meds = parse_llm_json(meds_raw)

                summary.admission_medications = meds.get(
                    "admission_medications",
                    []
                )

                summary.discharge_medications = meds.get(
                    "discharge_medications",
                    []
                )

                    
            if not summary.patient_demographics:

                clinical_raw = clinical_tool.run(
                    combined_text
                )

                planner.add_trace(
                    step,
                    "Need demographics, dates, hospital course, procedures and allergies",
                    "ClinicalExtractorTool",
                    "Patient Notes",
                    clinical_raw,
                    "Update Summary"
                )

                clinical = parse_llm_json(
                    clinical_raw
                )

                summary.patient_demographics = (
                    clinical.get(
                        "patient_demographics",
                        "Missing – Requires Clinician Review"
                    )
                )

                summary.admission_date = (
                    clinical.get(
                        "admission_date",
                        "Missing – Requires Clinician Review"
                    )
                )

                summary.discharge_date = (
                    clinical.get(
                        "discharge_date",
                        "Missing – Requires Clinician Review"
                    )
                )

                summary.hospital_course = (
                    clinical.get(
                        "hospital_course",
                        "Missing – Requires Clinician Review"
                    )
                )

                summary.procedures = (
                    clinical.get(
                        "procedures",
                        []
                    )
                )

                summary.allergies = (
                    clinical.get(
                        "allergies",
                        []
                    )
                )

            summary.medication_changes = (
                MedicationReconciliation.reconcile(
                    summary.admission_medications,
                    summary.discharge_medications
                )
            )

            pending_raw = pending_tool.run(combined_text)

            pending = parse_llm_json(pending_raw)

            if isinstance(pending, list):
                summary.pending_results = pending
            else:
                summary.pending_results = []

            summary.conflicts = (
                ConflictDetectorTool.detect(
                    documents
                )
            )
            
            break

        summary.safety_flags = (
            SafetyValidator.validate(summary)
        )

        warnings = DrugInteractionTool.check(
            summary.discharge_medications
        )

        summary.safety_flags.extend(warnings)

        txt_summary = SummaryGenerator.generate(summary)

        os.makedirs("outputs", exist_ok=True)

        with open(
            "outputs/summary.json",
            "w"
        ) as f:
            json.dump(
                summary.model_dump(),
                f,
                indent=2
            )

        with open(
            "outputs/trace.json",
            "w"
        ) as f:
            json.dump(
                planner.trace,
                f,
                indent=2
            )

        with open(
            "outputs/discharge_summary.txt",
            "w"
        ) as f:
            f.write(txt_summary)

        st.success("Agent Completed")

        st.subheader("Agent Trace")
        st.json(planner.trace)

        st.subheader("Generated Discharge Summary")
        st.text_area(
            "Summary",
            txt_summary,
            height=500
        )

        st.download_button(
            "Download Summary JSON",
            open("outputs/summary.json", "rb"),
            "summary.json"
        )

        st.download_button(
            "Download Trace JSON",
            open("outputs/trace.json", "rb"),
            "trace.json"
        )

        st.download_button(
            "Download Text Summary",
            open(
                "outputs/discharge_summary.txt",
                "rb"
            ),
            "discharge_summary.txt"
        )