from crewai import Process
from src.crew import crew


def test_crew_has_five_agents():
    assert len(crew.agents) == 5


def test_crew_has_five_tasks():
    assert len(crew.tasks) == 5


def test_crew_memory_enabled():
    assert crew.memory is True


def test_crew_default_sequential():
    assert crew.process == Process.sequential


def test_task_dependencies():
    from src.tasks import (
        research_task, fact_check_task, writing_task, editing_task, seo_task,
    )
    assert research_task in fact_check_task.context
    assert fact_check_task in writing_task.context
    assert writing_task in editing_task.context
    assert editing_task in seo_task.context
