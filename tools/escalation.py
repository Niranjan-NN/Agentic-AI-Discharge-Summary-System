class ClinicianEscalationTool:

    @staticmethod
    def escalate(issue):

        return {
            "status": "Clinician Review Required",
            "issue": issue
        }