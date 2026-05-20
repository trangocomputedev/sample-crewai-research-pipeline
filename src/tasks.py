import os
from crewai import Task
from src.agents import research_agent, fact_check_agent, writer_agent, editor_agent, seo_agent

os.makedirs("outputs", exist_ok=True)

research_task = Task(
    description=(
        "Research {topic} thoroughly. Find at least 5 reputable sources. "
        "Summarize key findings, statistics, and expert opinions."
    ),
    expected_output="A structured research report with bullet points per source and a synthesis section.",
    agent=research_agent,
    output_file="outputs/research.md",
)

fact_check_task = Task(
    description=(
        "Review the research report and verify each major claim. "
        "Mark each claim as VERIFIED, UNVERIFIED, or DISPUTED with source citations."
    ),
    expected_output="An annotated research report with verification status for each claim.",
    agent=fact_check_agent,
    context=[research_task],
    output_file="outputs/fact_check.md",
)

writing_task = Task(
    description=(
        "Write a 1500-word article on {topic} using the verified research. "
        "Include an introduction, 3-4 body sections with subheadings, and a conclusion."
    ),
    expected_output="A complete draft article in Markdown format.",
    agent=writer_agent,
    context=[fact_check_task],
    output_file="outputs/draft.md",
)

editing_task = Task(
    description=(
        "Edit the draft article. Improve sentence variety, fix passive voice, "
        "ensure logical paragraph flow, and check factual consistency."
    ),
    expected_output="A polished, publication-ready article in Markdown.",
    agent=editor_agent,
    context=[writing_task],
    output_file="outputs/edited.md",
)

seo_task = Task(
    description=(
        "Optimize the edited article for SEO. Add a meta title (< 60 chars), "
        "meta description (< 160 chars), focus keyword usage, and internal link placeholders."
    ),
    expected_output="Final article with SEO metadata block prepended.",
    agent=seo_agent,
    context=[editing_task],
    output_file="outputs/final.md",
)
