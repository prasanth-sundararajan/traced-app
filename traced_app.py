import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 1. Load keys and tracing flags from .env
load_dotenv()

# Pre-flight check: ensure tracing environment variables are visible
if os.getenv("LANGSMITH_TRACING") != "true":
    print("Warning: LANGSMITH_TRACING is not set to 'true'. Traces will not be sent!")
else:
    print(f"Tracing enabled. Project target: {os.getenv('LANGSMITH_PROJECT')}")

# 2. Initialize the model
llm = ChatOpenAI(model="gpt-4o-mini")

# 3. Define 3 prompts with differing complexity (short, medium, long)
prompts = [
    "What is the capital of France? Answer in one word.",
    "Explain the concept of gravity in three simple sentences.",
    "Write a detailed, step-by-step 200-word explanation of how the Internet works, including DNS, TCP/IP, and web servers."
]

# 4. Invoke the model for each prompt and print results
for idx, prompt in enumerate(prompts, start=1):
    print(f"\n--- Run {idx} ---")
    print(f"Prompt: {prompt}")
    response = llm.invoke(prompt)
    print(f"Answer: {response.content}")