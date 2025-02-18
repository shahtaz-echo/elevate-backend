# Elevate - Self Learning Platform

Elevate is an open-source self-learning platform that enables users to generate, manage, and customize courses with AI assistance. The platform helps users organize reading materials, take notes, and engage in self-paced learning. Additionally, it provides AI-powered quizzes to strengthen learning progress.

## Features

### Authentication

- Signup
- Login
- Forgot Password
- Reset Password

### User Profile

- Retrieve user profile data
- Update profile information

### Course Management

- **Generate New Courses:**
  - Users specify interests:
    - Topic name
    - Level (Basic, Intermediate, Advanced)
    - Duration (Minimum: Basic - 2 weeks, Intermediate - 4 weeks, Advanced - 8 weeks)
  - System processes inputs and generates:
    - Course name
    - Description
    - Course type
    - Timeline
    - Modules with:
      - Titles
      - Descriptions
      - Completion status
      - Submodules (topics, articles, video tutorials, notes, etc.)
  - Users can:
    - Edit AI-generated courses
    - Mark submodules as complete
    - Take quizzes under submodules
    - Generate notes
    - Ask AI questions and save responses as reports

### Notes Management

- Organize notes
- Edit and update notes
- AI-assisted note generation
- Share notes

### Study Plan

- AI-assisted study planning

### AI-powered Quiz

- Generate quizzes on specific topics
- AI provides multiple-choice questions with answers
- Timed quiz submissions
- Tracks quiz performance

## Tech Stack

- **Backend:** FastAPI
- **Database:** PostgreSQL
- **AI Integration:** LLaMA (LLM API)
- **Authentication:** OAuth2 / JWT

## Installation

### Prerequisites

- Python 3.9+
- Virtual environment (`venv` or `conda`)
- FastAPI
- PostgreSQL

### Setup

```bash
# Clone the repository
git clone https://github.com/shahtaz-echo/elevate-backend
cd elevate-backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload
```

## API Endpoints

### Authentication

| Method | Endpoint              | Description               |
| ------ | --------------------- | ------------------------- |
| POST   | /auth/register        | Register a new user       |
| POST   | /auth/login           | Authenticate user         |
| POST   | /auth/forgot-password | Send token to email       |
| POST   | /auth/reset-password  | Reset password with token |

### User Profile

| Method | Endpoint      | Description             |
| ------ | ------------- | ----------------------- |
| GET    | /user/profile | Retrieve user data      |
| PUT    | /user/update  | Update user information |

### Course Management

| Method | Endpoint         | Description                    |
| ------ | ---------------- | ------------------------------ |
| POST   | /course/generate | Generate AI-assisted course    |
| PUT    | /course/update   | Update course details          |
| GET    | /course/list     | List all courses               |
| POST   | /course/complete | Mark course/module as complete |

### Notes

| Method | Endpoint      | Description         |
| ------ | ------------- | ------------------- |
| POST   | /notes/create | Create a new note   |
| GET    | /notes/list   | Retrieve notes      |
| PUT    | /notes/update | Update note content |

### Quiz

| Method | Endpoint       | Description               |
| ------ | -------------- | ------------------------- |
| POST   | /quiz/generate | Generate a quiz via AI    |
| POST   | /quiz/submit   | Submit quiz answers       |
| GET    | /quiz/results  | Retrieve quiz performance |
