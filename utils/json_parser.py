# utils/json_parser.py

import json
import re


def parse_llm_json(response_text):

    try:

        cleaned = re.sub(
            r"```json|```",
            "",
            response_text
        ).strip()

        return json.loads(cleaned)

    except Exception as e:

        return {
            "error": str(e),
            "raw": response_text
        }