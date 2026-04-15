## MultiAgentJobSearchSystem

### Setup

- **Python**: Use **Python 3.13** (CrewAI’s current published requirement is Python `<3.14`).

Create a virtual environment and install deps:

```bash
python3.13 -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
```

### Run (Streamlit)

```bash
. .venv/bin/activate
streamlit run streamlit_app.py
```

### Technologies
Django Python OpenAI

The job market is competitive, and nearly every employer now expects AI skills. Building an AI-powered job application assistant that automates your entire job search. In this project, we'll create a multi-agent system using CrewAI, Python, and Streamlit that handles everything from analyzing job descriptions to drafting personalized LinkedIn outreach messages, saving time while showcasing your AI workflow automation capabilities to potential employers.

We'll build specialized AI agents using the CrewAI framework: a job analyzer that extracts key requirements from listings, a resume customization agent that tailors application materials, and a messaging agent that drafts professional outreach. We'll orchestrate these autonomous agents into a collaborative crew where each agent's output feeds into the next, creating an intelligent automation pipeline powered by LangChain and Google Gemini for natural language processing. We'll integrate the USAJobs API to fetch real government job postings and provide live data for the agents to work with.

Finally, we'll develop a Streamlit web application where you can input job preferences, browse fetched listings, select target positions, and generate customized resumes, cover letters, and LinkedIn messages with one click. We'll implement persistent logging to track applications and save generated materials. By the end, you'll have a portfolio-ready agentic system demonstrating CrewAI multi-agent orchestration, API integration, LLM-powered automation, and practical AI agent collaboration that proves your AI skills to recruiters.
