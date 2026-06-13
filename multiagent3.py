class ResearchAgent:
    def research(self, topic):
        return f"{topic} is transforming industries through automation and intelligence."

class WriterAgent:
    def write_article(self, research_data):
        return f"Article:\n{research_data}"

class ReviewerAgent:
    def review(self, article):
        return article + "\n\nReview Status: Approved"

research_agent = ResearchAgent()
writer_agent = WriterAgent()
reviewer_agent = ReviewerAgent()

research = research_agent.research("Artificial Intelligence")
article = writer_agent.write_article(research)
final_article = reviewer_agent.review(article)

print(final_article)