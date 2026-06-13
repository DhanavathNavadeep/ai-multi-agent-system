from research_agent import ResearchAgent
from writer_agent import WriterAgent
from reviewer_agent import ReviewerAgent

research_agent = ResearchAgent()
writer_agent = WriterAgent()
reviewer_agent = ReviewerAgent()

topic = "Artificial Intelligence"

research = research_agent.research(topic)
article = writer_agent.write_article(research)
final_article = reviewer_agent.review(article)

print(final_article)