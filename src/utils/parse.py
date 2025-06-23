import traceback
from typing import Dict

import httpx


def parse_resume(resume_file: bytes) -> Dict:
    """Parse a resume file

    Args:
        resume_file (bytes): The binary content of the resume file

    Returns:
        str: The parsed resume data
    """
    url = "https://cogent-labs.hirestream.io/api/v1/workflows/upload/?timezone=Asia%2FKarachi"

    try:
        with httpx.Client(timeout=30) as client:
            # Send both file and type in the form data
            files = {"file": ("resume.pdf", resume_file, "application/pdf")}
            data = {"type": "cv"}
            response = client.post(url, files=files, data=data)

            if response.status_code >= 400:
                raise Exception(f"API Error {response.status_code}: {response.text}")

            return response.json()
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}
