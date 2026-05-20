import os
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from src.agents import research_agent, fact_check_agent, writer_agent, editor_agent, seo_agent
from src.tasks import research_task, fact_check_task, writing_task, editing_task, seo_task

process_mode = os.getenv("CREW_PROCESS", "sequential")

crew = Crew(
    agents=[research_agent, fact_check_agent, writer_agent, editor_agent, seo_agent],
    tasks=[research_task, fact_check_task, writing_task, editing_task, seo_task],
    process=Process.sequential if process_mode == "sequential" else Process.hierarchical,
    manager_llm=ChatOpenAI(model="gpt-4o") if process_mode == "hierarchical" else None,
    memory=True,
    verbose=True,
    output_log_file="outputs/crew_log.txt",
)
