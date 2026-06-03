class SafetyValidator:

    @staticmethod
    def validate(summary):

        flags = []

        if not summary.principal_diagnosis:
            flags.append("Missing Principal Diagnosis")

        if not summary.admission_date:
            flags.append("Missing Admission Date")

        if not summary.discharge_date:
            flags.append("Missing Discharge Date")

        if not summary.allergies:
            flags.append("Missing Allergy Information")

        return flags