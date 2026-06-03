from pydantic import BaseModel
from typing import List, Dict, Any


class AgentTrace(BaseModel):
    step: int
    reasoning: str
    tool: str
    input: str
    result: str
    next_decision: str


class ConflictRecord(BaseModel):
    field: str
    values: List[str]
    status: str


class DischargeSummary(BaseModel):
    patient_demographics: str = ""
    admission_date: str = ""
    discharge_date: str = ""

    principal_diagnosis: str = ""
    secondary_diagnoses: List[str] = []

    hospital_course: str = ""
    procedures: List[str] = []

    admission_medications: List[str] = []
    discharge_medications: List[str] = []

    medication_changes: List[Dict] = []

    allergies: List[str] = []

    follow_up_instructions: str = ""

    pending_results: List[str] = []

    discharge_condition: str = ""

    safety_flags: List[str] = []

    conflicts: List[Dict] = []

    missing_fields: List[str] = []