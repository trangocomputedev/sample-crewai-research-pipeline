from src.agents import research_agent, fact_check_agent, writer_agent, editor_agent, seo_agent


def test_research_agent_role():
    assert research_agent.role == "Senior Research Analyst"


def test_fact_check_agent_role():
    assert fact_check_agent.role == "Fact Checker"


def test_research_agent_has_two_tools():
    assert len(research_agent.tools) == 2


def test_fact_check_agent_has_one_tool():
    assert len(fact_check_agent.tools) == 1


def test_writer_agent_has_file_tool():
    assert len(writer_agent.tools) == 1


def test_editor_and_seo_have_no_tools():
    assert len(editor_agent.tools) == 0
    assert len(seo_agent.tools) == 0


def test_seo_agent_uses_mini_model():
    assert "mini" in seo_agent.llm.model_name.lower()


def test_no_agent_allows_delegation():
    for agent in [research_agent, fact_check_agent, writer_agent, editor_agent, seo_agent]:
        assert agent.allow_delegation is False


def test_research_agent_max_iter():
    assert research_agent.max_iter == 5
