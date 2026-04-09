class LearningPathEvaluator:

    def reset(self):
        self.current_task = None
        self.score = 0
        return "\nEnvironment ready. Send a student study log to evaluate."
    
    def step(self, action):
        if self.current_task == "easy":
            score = self.grade_easy(
                student_log=action["student_log"],
                target=action["target"],
                agent_answer=action["agent_answer"]
            )
            self.score = score
            done = True
            return {
                "score": score,
                "done": done,
                "feedback":"Agent answered: " + action["agent_answer"]
            }
        
        elif self.current_task == "medium":
            score = self.grade_medium(
                student_log=action["student_log"],
                target=action["target"],
                agent_answer=action["agent_answer"]
            )
            self.score = score
            done = True
            return {
                "score": score,
                "done": done,
                "feedback": "Agent answered: " + str(action["agent_answer"]) # list can not be concatenated, str converts everything into string
            }
        
        elif self.current_task == "hard":
            score = self.grade_hard(
                student_log = action["student_log"],
                target = action["target"],
                agent_answer = action["agent_answer"]
            )
            self.score = score
            done = True
            return {
                "score": score,
                "done": done,
                "feedback": "Agent answered: " + str(action["agent_answer"])
            }

    def state(self):
        return {
            "current task": self.current_task,
            "score": self.score
        }
    
    def grade_easy(self, student_log, target, agent_answer):
        correct_order_so_far = CORRECT_ORDER[:CORRECT_ORDER.index(target)]
        if student_log == correct_order_so_far:
            correct_answer = "on track"
        else:
            correct_answer = "off track"

        if agent_answer == correct_answer:
            return 0.9
        else:
            return 0.1
        
    def grade_medium(self, student_log, target, agent_answer):
        target_index = CORRECT_ORDER.index(target)
        required_topics = CORRECT_ORDER[:target_index]
        missing_topics = [t for t in required_topics if t not in student_log] # if there is any topic in required_topics that's not in student log, add that to missing_topics

        if len(missing_topics) == 0:
            return 0.9
        
        if (agent_answer == missing_topics):
            return 0.9
        elif any(topic in agent_answer for topic in missing_topics): #if any of the missing topics appear somewhere in the agent's answer — even if not all of them — return 0.5.
            return 0.5
        else:
            return 0.1
        
    def grade_hard(self, student_log, target, agent_answer):
        target_index = CORRECT_ORDER.index(target)
        required_topics = CORRECT_ORDER[:target_index]
        missing_topics = [t for t in required_topics if t not in student_log] 
        out_of_order = [t for t in student_log if CORRECT_ORDER.index(t) > target_index]

        score = 0.1
        if missing_topics and any(t in agent_answer for t in missing_topics):
            score += 0.4
        if out_of_order and any(t in agent_answer for t in out_of_order):
            score += 0.4

        return score
    
CORRECT_ORDER = [
    "arrays",
    "linked lists",
    "stacks",
    "trees",
    "graphs",
    "dynamic programming"
]

    


    
