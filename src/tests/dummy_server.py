from contextlib import asynccontextmanager

import pytest
import uvicorn
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


async def parse_resume():
    return {
        "url": "temp/09:14:24.075075/resume.pdf",
        "temp_url": "https://hirestream-prod-multitenant-vxq3ibja.s3.amazonaws.com/temp/09%3A14%3A24.075075/resume.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQKO2WDLLJ5KX4U5Q%2F20250611%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20250611T091431Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=9edbc9b48149702a9e8645cd2fabbb2d8e674737e9b1a2872ec22a6fc6aa3494",
        "first_name": "SAFIULLAH",
        "last_name": "HUMAYUN",
        "email": "safihum99@gmail.com",
        "phone": "+92 3474480814",
        "address": "207-A Iqbal Avenue, phase 3, Lahore, Pakistan",
        "city": "Lahore",
        "tagged_education": [
            {
                "org": "National University of Sciences and Technology (NUST), Rawalpindi",
                "degree": "Bachelors in Computer Engineering",
                "start_date": "",
                "end_date": "",
                "current degree?": True,
            }
        ],
        "education_raw_txt": "",
        "skills": [
            {"id": 1260, "title": "artificial intelligence"},
            {"id": 1300, "title": "FastAPI"},
            {"id": 324, "title": "Flutter"},
            {"id": 325, "title": "Python"},
            {"id": 327, "title": "C++"},
            {"id": 338, "title": "GIT"},
            {"id": 357, "title": "Python"},
            {"id": 365, "title": "C++"},
            {"id": 374, "title": "tensorflow"},
            {"id": 416, "title": "mongodb"},
            {"id": 434, "title": "flutter"},
            {"id": 438, "title": "pytorch"},
            {"id": 440, "title": "opencv"},
            {"id": 441, "title": "flask"},
            {"id": 442, "title": "mysql"},
            {"id": 450, "title": "c++"},
            {"id": 452, "title": "PyTorch"},
            {"id": 481, "title": "git"},
            {"id": 484, "title": "keras"},
            {"id": 953, "title": "hugging face"},
            {"id": 1127, "title": "dart"},
            {"id": 762, "title": "Data Structures"},
            {"id": 1521, "title": "git"},
            {"id": 1531, "title": "MongoDB"},
            {"id": 1535, "title": "fastapi"},
            {"id": 1550, "title": "MySQL"},
            {"id": 1551, "title": "c++"},
            {"id": 1555, "title": "Python"},
            {"id": 1561, "title": "Flutter"},
            {"id": 1580, "title": "flask"},
            {"id": 1674, "title": "dart"},
            {"id": 1917, "title": "openCV"},
            {"id": 1930, "title": "artificial intelligence"},
            {"id": 1931, "title": "digital image processing"},
            {"id": 2030, "title": "Langchain"},
            {"id": 2077, "title": "Pytorch"},
            {"id": 2285, "title": "Tensorflow"},
            {"id": 2286, "title": "Keras"},
            {"id": 2301, "title": "LangChain"},
            {"id": 6320, "title": "langchain"},
            {"id": 3121, "title": "Tensorflow"},
            {"id": 3291, "title": "python"},
            {"id": 3323, "title": "Flask"},
            {"id": 3527, "title": "MySQL"},
            {"id": 3687, "title": "python"},
            {"id": 3802, "title": "Fastapi"},
            {"id": 4158, "title": "hugging face"},
            {"id": 4332, "title": "Mysql"},
            {"id": 4333, "title": "Mongodb"},
            {"id": 4391, "title": "git"},
            {"id": 4393, "title": "python"},
            {"id": 4507, "title": "git"},
            {"id": 4517, "title": "MongoDB"},
            {"id": 4521, "title": "fastapi"},
            {"id": 4536, "title": "MySQL"},
            {"id": 4537, "title": "c++"},
            {"id": 4541, "title": "Python"},
            {"id": 4547, "title": "Flutter"},
            {"id": 4566, "title": "flask"},
            {"id": 4650, "title": "dart"},
            {"id": 4865, "title": "openCV"},
            {"id": 4879, "title": "artificial intelligence"},
            {"id": 4880, "title": "digital image processing"},
            {"id": 4930, "title": "Langchain"},
            {"id": 4954, "title": "Pytorch"},
            {"id": 5022, "title": "Tensorflow"},
            {"id": 5023, "title": "Keras"},
            {"id": 5489, "title": "Flask"},
            {"id": 5695, "title": "python"},
            {"id": 5804, "title": "Fastapi"},
            {"id": 5992, "title": "hugging face"},
            {"id": 6447, "title": "PyTorch"},
            {"id": 6502, "title": "git"},
            {"id": 6512, "title": "MongoDB"},
            {"id": 6516, "title": "fastapi"},
            {"id": 6531, "title": "MySQL"},
            {"id": 6532, "title": "c++"},
            {"id": 6536, "title": "Python"},
            {"id": 6542, "title": "Flutter"},
            {"id": 6561, "title": "flask"},
            {"id": 6645, "title": "dart"},
            {"id": 6860, "title": "openCV"},
            {"id": 6874, "title": "artificial intelligence"},
            {"id": 6875, "title": "digital image processing"},
            {"id": 6925, "title": "Langchain"},
            {"id": 6949, "title": "Pytorch"},
            {"id": 7017, "title": "Tensorflow"},
            {"id": 7018, "title": "Keras"},
            {"id": 7484, "title": "Flask"},
            {"id": 7690, "title": "python"},
            {"id": 7799, "title": "Fastapi"},
            {"id": 7987, "title": "hugging face"},
        ],
        "tagged_employment": [
            {
                "org": "Octaloop Technologies",
                "designation": "AI Developer",
                "start_date": "2024-02-01",
                "end_date": "Present",
                "current_job": True,
            },
            {
                "org": "Freelancing",
                "designation": "Flutter Application Development",
                "start_date": "2022-09-01",
                "end_date": "Present",
                "current_job": True,
            },
            {
                "org": "Munzesta Solutions",
                "designation": "Intern - Mobile Application Development",
                "start_date": "2020-09-01",
                "end_date": "2020-12-01",
                "current_job": False,
            },
        ],
        "employment_raw_txt": "",
        "parsed_json_url": "parsed/50901047a7184f82899ed5e16923a74f.json",
        "cv_parsed_by": "arbisoft",
    }


@app.get("/jobs/published-jobs/")
async def list_jobs():
    return {
        "count": 7,
        "next": None,
        "previous": None,
        "results": [
            {
                "id": 663,
                "uuid": "a0871d6f-b1c0-4d03-b2b6-4866e50cd5b5",
                "title": "Staff Engineer",
                "department": "Software Development Department",
                "location": "552 College Road, Block 15, Sector B-1, Lahore",
                "positions": 1,
                "is_remote": False,
                "priority": 1,
            },
            {
                "id": 700,
                "uuid": "e27f2dbb-8421-4ade-bddb-98abbf499bf0",
                "title": "Technical Lead",
                "department": "HR & Admin Department",
                "location": "552 College Road, Block 15, Sector B-1, Lahore",
                "positions": 1,
                "is_remote": False,
                "priority": 1,
            },
            {
                "id": 784,
                "uuid": "c73f7dab-5068-4c64-a202-b8aea8901788",
                "title": "Social Media Associate",
                "department": "Marketing Department",
                "location": "552 College Road, Block 15, Sector B-1, Lahore",
                "positions": 1,
                "is_remote": False,
                "priority": 1,
            },
            {
                "id": 706,
                "uuid": "9c91c7ec-cf47-419e-b24d-0f805326faef",
                "title": "Upwork Bidder",
                "department": "Business Development Department",
                "location": "552 College Road, Block 15, Sector B-1, Lahore",
                "positions": 1,
                "is_remote": False,
                "priority": 1,
            },
            {
                "id": 669,
                "uuid": "d613f990-081e-4943-93e3-2e0ac822a36c",
                "title": "React JS Developer",
                "department": "Software Development Department",
                "location": "552 College Road, Block 15, Sector B-1, Lahore",
                "positions": 1,
                "is_remote": False,
                "priority": 1,
            },
            {
                "id": 399,
                "uuid": "dbbf23d7-fa70-41e3-8a09-8e80254547c6",
                "title": "Python/Django Developer",
                "department": "Software Development Department",
                "location": "552 College Road, Block 15, Sector B-1, Lahore",
                "positions": 1,
                "is_remote": False,
                "priority": 3,
            },
            {
                "id": 648,
                "uuid": "3dedfe23-4be6-4abf-8f99-3d2c8558db41",
                "title": "SQA Engineer",
                "department": "SQA Department",
                "location": "552 College Road, Block 15, Sector B-1, Lahore",
                "positions": 1,
                "is_remote": False,
                "priority": 8,
            },
        ],
        "departments": [
            {"title": "Software Development Department", "id": 275, "job_count": 3},
            {"title": "Design Department", "id": 276, "job_count": 0},
            {"title": "HR & Admin Department", "id": 277, "job_count": 1},
            {"title": "Business Development Department", "id": 278, "job_count": 1},
            {"title": "SQA Department", "id": 305, "job_count": 1},
            {"title": "Marketing Department", "id": 306, "job_count": 1},
            {"title": "Sales & Marketing", "id": 310, "job_count": 0},
            {"title": "Generative AI Department", "id": 403, "job_count": 0},
        ],
    }


@app.get("/jobs/c73f7dab-5068-4c64-a202-b8aea8901788/view-job/")
async def view_job():
    return {
        "id": 784,
        "uuid": "c73f7dab-5068-4c64-a202-b8aea8901788",
        "title": "Social Media Associate",
        "description": "%3Cp%3E%3Cstrong%3ECogent%20Labs%20is%20looking%20for%20a%20Social%20Media%20Associate%20for%20its%20Lahore%20office.%3C/strong%3E%3C/p%3E%0A%3Cp%3E%3Cbr%3E%3C/p%3E%0A%3Cp%3E%3Cstrong%3EKey%20Responsibilities%3A%3C/strong%3E%3C/p%3E%0A%3Cul%3E%0A%20%20%3Cli%3ECapture%20and%20edit%20event%20photos/videos%20for%20LinkedIn%20%26amp%3B%20Instagram%3C/li%3E%0A%20%20%3Cli%3ERetouch%20photos%20to%20match%20brand%20style%3C/li%3E%0A%20%20%3Cli%3EEdit%20videos%20with%20strong%20storytelling%2C%20timing%2C%20and%20trend%20alignment%3C/li%3E%0A%20%20%3Cli%3EMaintain%20a%20well-organized%20media%20library%3C/li%3E%0A%20%20%3Cli%3EOptimize%20content%20for%20different%20platforms%3C/li%3E%0A%20%20%3Cli%3EWork%20closely%20with%20the%20content/marketing%20team%3C/li%3E%0A%3C/ul%3E%0A%3Cp%3E%3Cstrong%3EMust-Have%3A%3C/strong%3E%3C/p%3E%0A%3Cul%3E%0A%20%20%3Cli%3E0%20to%202%20years%20of%20experience%20in%20visual%20storytelling%20or%20a%20strong%20passion%20for%20it%3C/li%3E%0A%20%20%3Cli%3EProficiency%20in%20Canva%2C%20Adobe%20Photoshop%2C%20Adobe%20Premiere%20Pro%3C/li%3E%0A%20%20%3Cli%3EStrong%20visual%20sense%20and%20editing%20skills%20%28Photo%20%26amp%3B%20Video%29%3C/li%3E%0A%20%20%3Cli%3EPeople-oriented%20with%20good%20communication%3C/li%3E%0A%20%20%3Cli%3EPortfolio%20showcasing%20both%20photography%20and%20videography%20work%3C/li%3E%0A%3C/ul%3E%0A%3Cp%3E%3Cstrong%3EGood%20to%20Have%3A%3C/strong%3E%3C/p%3E%0A%3Cul%3E%0A%20%20%3Cli%3ESelf-accountability%3C/li%3E%0A%20%20%3Cli%3EFamiliarity%20with%20platform-specific%20trends%3C/li%3E%0A%3C/ul%3E%0A%3Cp%3E%3Cstrong%3EDeal%20Breakers%3A%3C/strong%3E%3C/p%3E%0A%3Cul%3E%0A%20%20%3Cli%3EPoor%20communication%3C/li%3E%0A%20%20%3Cli%3ENo%20editing%20software%20knowledge%3C/li%3E%0A%20%20%3Cli%3ENo%20relevant%20portfolio%3C/li%3E%0A%3C/ul%3E%0A%3Cp%3E%3Cstrong%3EAttractive%20Perks%3A%3C/strong%3E%3C/p%3E%0A%3Cul%3E%0A%20%20%3Cli%3EDaily%20lunch%2C%20performance%20bonuses%2C%20medical%20coverage%2C%20financial%20assistance%2C%20travel%20allowance%20and%20much%20more%3C/li%3E%0A%3C/ul%3E%0A%3Cp%3E%3Cstrong%3ECultural%20Fit%3A%3C/strong%3E%3C/p%3E%0A%3Cul%3E%0A%20%20%3Cli%3EInclusive%20approach%2C%20high%20energy%20and%20integrity%2C%20Attention%20to%20detail%3C/li%3E%0A%3C/ul%3E",
        "requirements": [
            {
                "id": 1134,
                "title": "Employment",
                "status": "required",
                "type": "employment",
                "restrictions": None,
                "options": [],
            },
            {
                "id": 1135,
                "title": "Education",
                "status": "required",
                "type": "education",
                "restrictions": None,
                "options": [],
            },
            {
                "id": 1136,
                "title": "Professional Experience (in months)",
                "status": "required",
                "type": "number",
                "restrictions": None,
                "options": [
                    {"id": 134, "name": "6"},
                    {"id": 135, "name": "7"},
                    {"id": 136, "name": "8"},
                    {"id": 137, "name": "9"},
                    {"id": 138, "name": "10"},
                    {"id": 139, "name": "11"},
                    {"id": 140, "name": "12"},
                    {"id": 141, "name": "More"},
                    {"id": 142, "name": "1"},
                    {"id": 143, "name": "2"},
                    {"id": 144, "name": "3"},
                    {"id": 145, "name": "4"},
                    {"id": 146, "name": "5"},
                    {"id": 147, "name": "13"},
                    {"id": 148, "name": "14"},
                    {"id": 149, "name": "15"},
                    {"id": 150, "name": "16"},
                    {"id": 151, "name": "17"},
                    {"id": 152, "name": "18"},
                    {"id": 153, "name": "19"},
                    {"id": 154, "name": "20"},
                    {"id": 155, "name": "21"},
                    {"id": 156, "name": "22"},
                    {"id": 157, "name": "23"},
                    {"id": 158, "name": "24"},
                    {"id": 165, "name": "Fresh"},
                ],
            },
            {
                "id": 1131,
                "title": "Current Salary",
                "status": "required",
                "type": "number",
                "restrictions": None,
                "options": [],
            },
            {
                "id": 1132,
                "title": "Expected Salary",
                "status": "required",
                "type": "number",
                "restrictions": None,
                "options": [],
            },
            {
                "id": 1133,
                "title": "Availability to Join (in days)",
                "status": "required",
                "type": "number",
                "restrictions": None,
                "options": [],
            },
            {
                "id": 1138,
                "title": "Portfolio",
                "status": "required",
                "type": "link",
                "restrictions": None,
                "options": [],
            },
            {
                "id": 1137,
                "title": "I confirm that the information provided by me is accurate and complete to the best of my knowledge. I understand that I will be held accountable for any discrepancies or changes made.",
                "status": "required",
                "type": "dropdownmenu",
                "restrictions": None,
                "options": [{"id": 166, "name": "Yes"}, {"id": 167, "name": "No"}],
            },
        ],
        "location": "552 College Road, Block 15, Sector B-1, Lahore, Lahore",
        "department": {"id": 306, "title": "Marketing Department"},
        "source_types": {
            "referral": "Referral",
            "website": "Company Website",
            "jobboard": "Job Board",
            "socialmedia": "Social Media",
            "other": "Other",
            "searchfirm": "Search Firm",
            "externalreferral": "External Referral",
        },
        "skills": [
            {"id": 8312, "title": "Adaptability to Changing Requirements"},
            {"id": 8313, "title": "Ownership & Accountability"},
            {"id": 8314, "title": "AI automations"},
            {"id": 8315, "title": "qdrant"},
            {"id": 8318, "title": "teching"},
            {"id": 8319, "title": "MS SQL Server"},
        ],
        "job_status": "publish",
        "is_linkedin_required": True,
    }


@app.post("/workflows/job-applications/")
async def apply_to_job():
    return {
        "message": "Application submitted successfully",
    }


# Test client fixture
@pytest.fixture
def test_client():
    return TestClient(app)


def run_test_server(host: str = "127.0.0.1", port: int = 8000):
    """Run the test server on the specified host and port."""
    uvicorn.run(app, host=host, port=port)


@asynccontextmanager
async def get_test_client():
    """Async context manager to get a test client."""
    async with TestClient(app) as client:
        yield client


if __name__ == "__main__":
    run_test_server()
