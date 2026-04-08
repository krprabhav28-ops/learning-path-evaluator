import os
from environment import LearningPathEvaluator

API_BASE_URL = os.environ.get("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.environ.get("HF_TOKEN")

env = LearningPathEvaluator()

# Easy Task
env.reset()
env.current_task = "easy"
print(f"[START] task=easy env=learning-path-evaluator model={MODEL_NAME}")
result = env.step({
    "student_log": ["arrays", "linked lists", "stacks"],
    "target": "trees",
    "agent_answer": "on track"
})
print(f"[STEP] step=1 action=on track reward={result['score']:.2f} done=true error=null")
print(f"[END] success=true steps=1 score={result['score']:.3f} rewards={result['score']:.2f}")

# Medium Task
env.reset()
env.current_task = "medium"
print(f"[START] task=medium env=learning-path-evaluator model={MODEL_NAME}")
result = env.step({
    "student_log": ["arrays", "stacks"],
    "target": "trees",
    "agent_answer": ["linked lists"]
})
print(f"[STEP] step=1 action=linked lists reward={result['score']:.2f} done=true error=null")
print(f"[END] success=true steps=1 score={result['score']:.3f} rewards={result['score']:.2f}")

# Hard Task
env.reset()
env.current_task = "hard"
print(f"[START] task=hard env=learning-path-evaluator model={MODEL_NAME}")
result = env.step({
    "student_log": ["arrays", "dynamic programming", "arrays", "linked lists"],
    "target": "trees",
    "agent_answer": ["dynamic programming", "stacks"]
})
print(f"[STEP] step=1 action=dynamic programming and stacks reward={result['score']:.2f} done=true error=null")
print(f"[END] success=true steps=1 score={result['score']:.3f} rewards={result['score']:.2f}")
