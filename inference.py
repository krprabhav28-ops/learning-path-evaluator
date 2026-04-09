import os
import ast
from openai import OpenAI
from environment import LearningPathEvaluator

API_BASE_URL = os.environ.get("API_BASE_URL") or "https://api.openai.com/v1"
MODEL_NAME = os.environ.get("MODEL_NAME") or "gpt-4o-mini"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=OPENAI_API_KEY
)

def ask_llm(prompt):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an AI that evaluates student learning paths."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

env = LearningPathEvaluator()

# EASY TASK
env.reset()
env.current_task = "easy"
print(f"[START] task=easy env=learning-path-evaluator model={MODEL_NAME}")

prompt = """
Student log: ["arrays", "linked lists", "stacks"]
Target: trees

Is the student on track? Answer ONLY: on track or off track.
"""
answer = ask_llm(prompt)

result = env.step({
    "student_log": ["arrays", "linked lists", "stacks"],
    "target": "trees",
    "agent_answer": answer.lower()
})

print(f"[STEP] step=1 action={answer} reward={result['score']:.2f} done=true error=null")
print(f"[END] success=true steps=1 score={result['score']:.3f} rewards={result['score']:.2f}")


# MEDIUM TASK
env.reset()
env.current_task = "medium"
print(f"[START] task=medium env=learning-path-evaluator model={MODEL_NAME}")

prompt = """
Student log: ["arrays", "stacks"]
Target: trees

Which prerequisite topics are missing?
Return ONLY a Python list like ["topic1", "topic2"].
"""
answer = ask_llm(prompt)

try:
    parsed_answer = ast.literal_eval(answer)
except:
    parsed_answer = []

result = env.step({
    "student_log": ["arrays", "stacks"],
    "target": "trees",
    "agent_answer": parsed_answer
})

print(f"[STEP] step=1 action={parsed_answer} reward={result['score']:.2f} done=true error=null")
print(f"[END] success=true steps=1 score={result['score']:.3f} rewards={result['score']:.2f}")


# HARD TASK
env.reset()
env.current_task = "hard"
print(f"[START] task=hard env=learning-path-evaluator model={MODEL_NAME}")

prompt = """
Student log: ["arrays", "dynamic programming", "arrays", "linked lists"]
Target: trees

Identify:
1. Missing prerequisite topics
2. Topics studied out of order

Return as a Python list.
"""
answer = ask_llm(prompt)

try:
    parsed_answer = ast.literal_eval(answer)
except:
    parsed_answer = []

result = env.step({
    "student_log": ["arrays", "dynamic programming", "arrays", "linked lists"],
    "target": "trees",
    "agent_answer": parsed_answer
})

print(f"[STEP] step=1 action={parsed_answer} reward={result['score']:.2f} done=true error=null")
print(f"[END] success=true steps=1 score={result['score']:.3f} rewards={result['score']:.2f}")
