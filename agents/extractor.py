from google import genai


class DiagnosisExtractorTool:

    def __init__(self, client):
        self.client = client

    def run(self, text):

        prompt = f"""
        Extract diagnoses.

        Return JSON:
        {{
            "principal": "",
            "secondary": []
        }}

        TEXT:
        {text[:15000]}
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text


class MedicationExtractorTool:

    def __init__(self, client):
        self.client = client

    def run(self, text):

        prompt = f"""
        Extract medications.

        Return JSON:
        {{
            "admission_medications": [],
            "discharge_medications": []
        }}

        TEXT:
        {text[:15000]}
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text


class PendingResultTool:

    def __init__(self, client):
        self.client = client

    def run(self, text):

        prompt = f"""
        Identify pending labs,
        pending investigations,
        pending pathology results.

        Return ONLY valid JSON.

        Example:

        [
        "Urine Culture",
        "CBC"
        ]

        No markdown.
        No explanation.

        TEXT:
        {text[:15000]}
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
    
class ClinicalExtractorTool:

    def __init__(self, client):
        self.client = client

    def run(self, text):

        prompt = f"""
You are a clinical information extraction system.

Extract the following fields.

Return ONLY valid JSON.

{{
    "patient_demographics":"",
    "admission_date":"",
    "discharge_date":"",
    "hospital_course":"",
    "procedures":[],
    "allergies":[]
}}

Rules:

- Never hallucinate.
- If unavailable use:
  "Missing – Requires Clinician Review"
- Return JSON only.
- No markdown.

CLINICAL NOTES:

{text[:30000]}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text