class ResearchAgent:
    def research(self, topic):
        return f"{topic} is transforming industries through automation and intelligence."

class WriterAgent:
    def write_article(self, research_data):
        article = f"""
# Artificial Intelligence

Introduction:
{research_data}

Conclusion:
AI will continue to shape the future.
"""
        return article

research_agent = ResearchAgent()
writer_agent = WriterAgent()

topic = "Artificial Intelligence"

research_data = research_agent.research(topic)
article = writer_agent.write_article(research_data)

print(article)