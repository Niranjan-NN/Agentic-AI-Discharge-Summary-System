from models.schemas import AgentTrace


class AgentPlanner:

    REQUIRED_FIELDS = [
        "principal_diagnosis",
        "admission_date",
        "discharge_date",
        "allergies",
        "discharge_medications"
    ]

    def __init__(self):

        self.trace = []

    def add_trace(
        self,
        step,
        reasoning,
        tool,
        input_data,
        result,
        next_decision
    ):

        self.trace.append(
            AgentTrace(
                step=step,
                reasoning=reasoning,
                tool=tool,
                input=input_data,
                result=result,
                next_decision=next_decision
            ).model_dump()
        )