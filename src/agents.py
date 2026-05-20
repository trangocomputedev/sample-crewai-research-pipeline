from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileReadTool
from langchain_openai import ChatOpenAI

research_agent = Agent(
    role="Senior Research Analyst",
    goal="Uncover comprehensive, accurate information about {topic} from reputable web sources",
    backstory=(
        "You are an expert researcher with 10 years of experience. "
        "You excel at finding primary sources and synthesizing complex information."
    ),
    llm=ChatOpenAI(model="gpt-4o"),
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
    verbose=True,
    allow_delegation=False,
    max_iter=5,
)

fact_check_agent = Agent(
    role="Fact Checker",
    goal="Verify all claims in the research findings with at least one additional source",
    backstory="You are a meticulous journalist who never publishes without verification.",
    llm=ChatOpenAI(model="gpt-4o"),
    tools=[SerperDevTool()],
    verbose=True,
    allow_delegation=False,
)

writer_agent = Agent(
    role="Senior Content Writer",
    goal="Write an engaging, well-structured 1500-word article on {topic}",
    backstory="You are a versatile writer who transforms research into compelling narratives.",
    llm=ChatOpenAI(model="gpt-4o"),
    tools=[FileReadTool()],
    verbose=True,
    allow_delegation=False,
)

editor_agent = Agent(
    role="Content Editor",
    goal="Refine the article for clarity, flow, and factual accuracy",
    backstory="You are a senior editor with an eye for engaging prose and logical structure.",
    llm=ChatOpenAI(model="gpt-4o"),
    tools=[],
    verbose=True,
    allow_delegation=False,
)

seo_agent = Agent(
    role="SEO Specialist",
    goal="Optimize the article for search engines while maintaining readability",
    backstory="You understand Google's algorithms and write meta descriptions that drive clicks.",
    llm=ChatOpenAI(model="gpt-4o-mini"),
    tools=[],
    verbose=True,
    allow_delegation=False,
)
