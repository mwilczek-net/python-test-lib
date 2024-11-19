from .format import skip_indentation


def test_skip_indentation() -> None:
    source_00 = "asdf"
    expected_00 = "asdf"

    source_01 = """
    Long text:
     - but formatted
     - according to code formatters

     Still we should be able
        to format it
    """

    expected_01 = """Long text:
 - but formatted
 - according to code formatters

 Still we should be able
    to format it"""

    assert skip_indentation(s=source_00) == expected_00
    assert skip_indentation(s=source_01) == expected_01