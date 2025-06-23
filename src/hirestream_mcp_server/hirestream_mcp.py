# server.py
import os
from typing import Dict

from hirestream_client import (HireStreamAPIClient, JobApplyRequest,
                               JobDetailsRequest, JobDetailsResponse,
                               JobListingResponse)
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

hirestream_client = HireStreamAPIClient(
    access_token=os.getenv("HIRESTREAM_ACCESS_TOKEN"),
    base_api_url=os.getenv("BASE_API_URL"),
)


@mcp.tool()
async def list_jobs() -> JobListingResponse:
    """
    Execute a swap transaction.

    Expects a SwapTransactionRequestContainer, returns a list of SwapTransactionResponse.
    """
    try:
        result: JobListingResponse = await hirestream_client.list_jobs()
        return result
    except Exception as e:
        return [{"error": str(e)}]


@mcp.tool()
async def show_job_details(
    job_details_request: JobDetailsRequest,
) -> JobDetailsResponse:
    """
    Execute a swap transaction.

    Expects a SwapTransactionRequestContainer, returns a list of SwapTransactionResponse.
    """
    try:
        result: JobDetailsResponse = await hirestream_client.show_job_details(
            job_details_request
        )
        return result
    except Exception as e:
        return [{"error": str(e)}]


@mcp.tool()
async def apply_to_job(job_apply_request: JobApplyRequest) -> Dict:
    """
    Apply to a job.

    First ask the user to upload the resume before he applies to the job.
    """
    try:
        result: JobDetailsResponse = await hirestream_client.apply_to_job(
            job_apply_request
        )
        return result
    except Exception as e:
        return [{"error": str(e)}]


def main():
    mcp.run()


if __name__ == "__main__":
    main()
