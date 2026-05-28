# Sample CrewAI Research Pipeline

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

A multi-agent content research and publication pipeline built with [CrewAI](https://github.com/crewAIInc/crewAI). Serves as a canonical example of CrewAI features and as a test fixture for the AI Workflow Visualizer.

## Workflow

```
[Research Agent] ──▶ [Fact-Check Agent] ──▶ [Writer Agent] ──▶ [Editor Agent] ──▶ [SEO Agent]
      │                     │                      │                  │                │
  (WebSearch,           (WebSearch)            (FileRead)         (no tools)       (no tools)
   ScrapeURL)
```

Each agent's output feeds directly into the next via `context=[previous_task]`, and intermediate results are written to `outputs/`.

## Sequential vs Hierarchical

Set `CREW_PROCESS=sequential` (default) for a linear pipeline, or `CREW_PROCESS=hierarchical` to have a `gpt-4o` manager agent plan and delegate tasks to the crew.

## Features Demonstrated

| CrewAI Feature | Location |
|---|---|
| `Agent(role, goal, backstory, llm, tools)` | `src/agents.py` |
| Multiple agents with different LLMs | `src/agents.py` |
| `Task(description, expected_output, agent, context)` | `src/tasks.py` |
| `context=[other_task]` inter-task dependency | `src/tasks.py` |
| `output_file` on tasks | `src/tasks.py` |
| `Crew(agents, tasks, process=Process.sequential)` | `src/crew.py` |
| `Crew(process=Process.hierarchical, manager_llm=...)` | `src/crew.py` |
| `memory=True` on Crew | `src/crew.py` |
| `SerperDevTool`, `ScrapeWebsiteTool`, `FileReadTool` | `src/agents.py` |
| Custom `BaseTool` subclass | `src/tools/custom_scraper.py` |

## Quickstart

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set credentials
cp .env.example .env
# Fill in OPENAI_API_KEY and SERPER_API_KEY

# 3. Run the pipeline
python main.py "the future of quantum computing"
```

Outputs are written to the `outputs/` directory:
- `outputs/research.md` — raw research report
- `outputs/fact_check.md` — annotated verification
- `outputs/draft.md` — initial article draft
- `outputs/edited.md` — polished article
- `outputs/final.md` — SEO-optimized final article

## Hierarchical Mode

```bash
CREW_PROCESS=hierarchical python main.py "renewable energy breakthroughs"
```

In hierarchical mode a manager agent (gpt-4o) orchestrates the crew, autonomously deciding which agent handles each part of the work.

## Tests

```bash
pytest tests/ -v
```

## Project Structure

```
src/
├── agents.py          # All Agent definitions
├── tasks.py           # All Task definitions with context dependencies
├── crew.py            # Crew assembly — the file the visualizer parses
└── tools/
    └── custom_scraper.py  # Example custom BaseTool
outputs/               # Generated at runtime (gitignored)
tests/
main.py
```

---

Built by [Trango Compute](https://trango-compute.com)
