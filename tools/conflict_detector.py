class ConflictDetectorTool:

    @staticmethod
    def detect(documents):

        conflicts = []

        diagnoses = []

        for doc in documents:

            text = doc.get(
                "text",
                ""
            ).upper()

            if "UTI" in text:
                diagnoses.append("UTI")

            if "DKA" in text:
                diagnoses.append("DKA")

            if "PNEUMONIA" in text:
                diagnoses.append("PNEUMONIA")

        unique_diagnoses = list(
            set(diagnoses)
        )

        if len(unique_diagnoses) > 1:

            conflicts.append(
                {
                    "field": "Diagnosis",
                    "values": unique_diagnoses,
                    "status":
                    "Clinician Review Required"
                }
            )

        return conflicts