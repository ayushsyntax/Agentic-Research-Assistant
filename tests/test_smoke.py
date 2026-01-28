def test_project_modules_importable():
    """
    Minimal smoke test to ensure core modules import without executing runtime logic.
    Does not require network access, APIs, models, or external processes.
    """
    import src.app
    import src.graph
    import src.tools
    import src.rag
    import src.llm
    import src.database
    import src.config

    # Test passes if imports succeed
    assert True
