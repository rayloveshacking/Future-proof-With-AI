# Futureproof with AI 🚀

**Hackathon Submission:** AisP Cyber & AI Hackathon

## Inspiration & Problem Statement 🤔

The rise of Artificial Intelligence is transforming industries, creating a demand for professionals who can leverage AI alongside their core skills. However, students often struggle to:

1.  Understand which AI skills are relevant to their desired career paths.
2.  Develop a clear roadmap to acquire these skills.
3.  Showcase their AI-enhanced capabilities effectively to potential employers.

Simultaneously, recruiters face challenges in identifying candidates who possess the right blend of domain expertise and practical AI knowledge.

**Futureproof with AI** aims to bridge this gap, empowering students to navigate the AI-driven job market and connecting recruiters with the next generation of AI-savvy talent.

## Our Solution ✨

Futureproof with AI is a web platform designed to be the **AI Career Co-pilot** for students and a talent pipeline for recruiters.

*   **For Students:** We help you identify your desired career path, map your existing skills, and generate a personalized, step-by-step AI learning roadmap. Build an AI-enhanced portfolio and get noticed by companies actively seeking your skills.
*   **For Recruiters:** Access a curated pool of students who are actively upskilling in AI relevant to industry needs. Define your required skill sets and find candidates ready to tackle tomorrow's challenges.

## Key Features 🎯

*   **Personalized AI Roadmap Generation:** Input your target role and current skills to receive a tailored learning path. (Core backend logic likely in `app/application/views.py`)
*   **AI Powered Chatbot:** Tailor roadmap to the needs of the students, then additionally advice can also be received.
*   **Portfolio Builder:** Showcase your projects and AI-enhanced skills. (Potentially linked to `upload.html` and models in `app/application/models.py`)
*   **Student Profile Discovery:** Recruiters can browse and filter student profiles based on skills and roadmap progress. (Related to `talent.html`)
*   **Recruiter Portal:** Companies can specify desired AI skills and connect with suitable candidates.
*   **Clean Landing Page:** Introduces the platform's value proposition (`landing_page.html`, `main_styling.css`).

## Tech Stack 💻

*   **Frontend:** HTML, CSS
*   **Backend:** Python, Django (`app/manage.py`, `app/app/`, `app/application/`)
*   **Database:** SQLite (`app/db.sqlite3` - default development DB)
*   **Version Control:** Git

## Getting Started ⚙️

To run this project locally:

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd Future-proof-With-AI
    ```
2.  **Set up a Python virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    *(Note: A `requirements.txt` file is recommended. Assuming standard Django setup)*
    ```bash
    pip install Django # Add other dependencies if listed in requirements.txt
    ```
4.  **Navigate to the Django project directory:**
    ```bash
    cd app
    ```
5.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```
6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
7.  Open your browser and go to `http://127.0.0.1:8000/` (or the landing page `../landing_page.html` for the static part).

## Future Plans 🔮

*   Integrate with specific AI APIs (e.g., OpenAI) for more dynamic roadmap generation and content suggestions.
*   Develop more sophisticated matching algorithms between students and recruiter requirements.
*   Add direct messaging features.
*   Expand the range of supported roles and skills.
*   Implement user authentication and profiles more robustly.

## Team 🧑‍💻

*   Thar Htet Shein
*   Jun Hao
*   Aldric Liew

---

*Built with passion during the AiSP Hackathon!*
