# LangChain and LangSmith Tracing Demo

## What this project is

A command-line example in [`traced_app.py`](./traced_app.py) that sends three questions of increasing length to the OpenAI `gpt-4o-mini` model using LangChain. When LangSmith tracing is enabled, the requests can be recorded in a LangSmith project for inspection.

## Requirements and configuration

Use Python 3.10 or newer. From PowerShell in this folder:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install python-dotenv langchain-openai
```

Create a local `.env` file with the required credentials and settings:

```dotenv
OPENAI_API_KEY=your_openai_key
LANGSMITH_API_KEY=your_langsmith_key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=your_project_name
```

Use your own key values and never commit or share them. The existing `.gitignore` ignores `.env`.

## Run it

```powershell
python .\traced_app.py
```

The script prints each prompt and model answer. If tracing is enabled, confirm that the three runs appear in the configured LangSmith project. API calls may incur charges.

## What still needs to be done

- Add a `requirements.txt` with tested dependency versions.
- Run once with valid credentials and confirm that all three answers and traces appear.
- Test the missing-tracing configuration and confirm the script's warning is understandable.
- Review screenshots before sharing them to make sure they do not expose API keys or private account information.
- Add automated tests or a mock model path so basic behavior can be tested without paid API calls.

## Task completed

The script sends three example prompts of different lengths to an OpenAI model and can send run details to a LangSmith project for tracing.

## Beginner task question

**Can you write a Python script that sends a few questions to an AI model, prints each answer, and records the runs in LangSmith so you can inspect them later?**

Try different prompt lengths, compare the answers and run details, and make sure your API keys stay in `.env` rather than in the Python file.
