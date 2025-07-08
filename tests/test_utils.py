import pytest

from src.utils.utils import mask_emails


@pytest.mark.parametrize("input_str, expected_output", [
    ("filip.kristofersson@vti.se", "[EMAIL]"),
])
def test_mask_emails(input_str, expected_output):
    result = mask_emails(input_str)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
