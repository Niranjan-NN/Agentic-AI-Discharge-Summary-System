class MedicationReconciliation:

    @staticmethod
    def reconcile(admission, discharge):

        changes = []

        admission_set = set(admission)
        discharge_set = set(discharge)

        for med in discharge_set - admission_set:
            changes.append(
                {
                    "type": "Added",
                    "medication": med,
                    "reason": "Reason Not Documented – Clinician Review Required"
                }
            )

        for med in admission_set - discharge_set:
            changes.append(
                {
                    "type": "Removed",
                    "medication": med,
                    "reason": "Reason Not Documented – Clinician Review Required"
                }
            )

        return changes