class SummaryGenerator:

    @staticmethod
    def generate(summary):

        disclaimer = """
AI Generated Draft.
Requires Clinician Review.
Do Not Use As Final Clinical Documentation.
"""

        text = f"""
{disclaimer}

PATIENT DEMOGRAPHICS
{summary.patient_demographics}

ADMISSION DATE
{summary.admission_date}

DISCHARGE DATE
{summary.discharge_date}

PRINCIPAL DIAGNOSIS
{summary.principal_diagnosis}

SECONDARY DIAGNOSES
{chr(10).join(summary.secondary_diagnoses)}

HOSPITAL COURSE
{summary.hospital_course}

PROCEDURES
{summary.procedures}

ALLERGIES
{chr(10).join(summary.allergies)}

DISCHARGE MEDICATIONS
{chr(10).join(summary.discharge_medications)}

MEDICATION CHANGES
{summary.medication_changes}

FOLLOW UP
{summary.follow_up_instructions}

PENDING RESULTS
{chr(10).join(summary.pending_results)}

SAFETY FLAGS
{summary.safety_flags}

CONFLICTS
{summary.conflicts}
"""
        return text