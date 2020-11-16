def test_version():
    import rsokl_dummy

    assert isinstance(rsokl_dummy.__version__, str)
    assert rsokl_dummy.__version__
    assert "unknown" not in rsokl_dummy.__version__

