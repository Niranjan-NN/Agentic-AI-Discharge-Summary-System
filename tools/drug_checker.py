class DrugInteractionTool:

    @staticmethod
    def check(medications):

        warnings = []

        mock_pairs = [
            ("warfarin", "aspirin"),
            ("insulin", "prednisone")
        ]

        meds = " ".join(medications).lower()

        for a, b in mock_pairs:

            if a in meds and b in meds:
                warnings.append(
                    f"Potential interaction detected: {a} + {b}"
                )

        return warnings