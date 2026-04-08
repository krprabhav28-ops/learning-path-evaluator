What does this environment simulate?

This environment simulates a learning path evaluator for self-directed students. An AI agent is given a student's study log and must assess whether the student is following the correct topic order, identify missing topics, and suggest corrections. The environment grades the agent's responses to provide reinforcement learning signals.

Why does this problem matter in real life?

Self-directed learners — especially those studying DSA online without guidance — frequently lose track of topic order, skip prerequisites, and jump to advanced topics too early. This kills motivation and creates knowledge gaps. An AI agent trained on this environment could help students stay on the correct learning path and complete their courses effectively.

_Tasks_

Easy — On Track or Off Track
The agent is given a student's completed topics list and a target topic. It must decide whether the student is on track or off track based on correct prerequisite order. Score: 1.0 for correct judgment, 0.0 for wrong.

Medium — Identify Missing Topics
The agent is given a messy study log with gaps and must identify exactly which prerequisite topics are missing before the target. Score: 1.0 for identifying all missing topics, 0.5 for partial identification, 0.0 for completely wrong.

Hard — Full Diagnosis
The agent is given a full week's study log with out-of-order topics, repetitions, and missing prerequisites. It must identify both what's missing and what was studied out of order. Score: 0.5 for identifying at least one out-of-order topic, 0.5 for identifying at least one missing topic, 1.0 for both.