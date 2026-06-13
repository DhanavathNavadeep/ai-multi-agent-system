class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def work(self, task):
        return f"{self.name} ({self.role}) completed: {task}"

research_agent = Agent("ResearchAgent", "Research")
writer_agent = Agent("WriterAgent", "Content Writer")

topic = "Artificial Intelligence"

research = research_agent.work(f"Researching {topic}")
article = writer_agent.work(f"Writing article using research")

print(research)
print(article)