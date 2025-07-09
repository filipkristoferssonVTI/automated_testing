import pytest

from src.example_package.example_module import mask_emails


# 1. Parametrize: Test multiple input/output pairs automatically
@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("Contact me at john.doe@example.com", "Contact me at [EMAIL]"),
        ("Emails: alice@mail.com, bob123@sub.domain.org", "Emails: [EMAIL], [EMAIL]"),
        ("No email here!", "No email here!"),
        ("Multiple: test1@test.com and test2@test.com", "Multiple: [EMAIL] and [EMAIL]"),
        ("Edge.case+foo@bar-baz.com", "[EMAIL]"),
        ("", ""),
    ]
)
def test_mask_emails_parametrized(input_text, expected):
    """Tests masking emails in various scenarios using parametrize."""
    assert mask_emails(input_text) == expected


# 2. Fixture: Example fixture that could be used for setup (not strictly needed here, but shown for demo)
@pytest.fixture
def email_samples():
    """Provides a list of sample emails for tests."""
    return [
        "first@example.com",
        "second@mail.org",
        "third.person@company.co.uk"
    ]


def test_mask_emails_from_fixture(email_samples):
    """Tests masking a list of emails provided by a fixture."""
    text = ", ".join(email_samples)
    expected = ", ".join(["[EMAIL]"] * len(email_samples))
    assert mask_emails(text) == expected


# 3. Test for skipping (e.g., a test you want to skip for now)
@pytest.mark.skip(reason="Demonstration of skipping a test")
def test_skip_example():
    assert mask_emails("a@b.com") == "[EMAIL]"


# 4. Test expected failure (xfail)
@pytest.mark.xfail(reason="Demonstration: This test is expected to fail")
def test_xfail_example():
    # This intentionally fails to show xfail usage
    assert mask_emails("no emails here") == "[EMAIL]"


# 5. Custom marker
@pytest.mark.slow
def test_long_text():
    """Simulates a slow test on a very long text just to show marker usage ('slow' is a custom pytest marker)."""
    text = "test.user{}@site.com ".format(12345) * 1000
    masked = mask_emails(text)
    assert masked.count("[EMAIL]") == 1000


# 6. Group tests in a class (useful for related test organization)
class TestMaskEmails:

    def test_multiline(self):
        """Tests masking emails across multiple lines."""
        text = "One: first@example.com\nTwo: second@site.org"
        expected = "One: [EMAIL]\nTwo: [EMAIL]"
        assert mask_emails(text) == expected

    def test_no_email(self):
        """Tests input with no emails at all."""
        input_text = "Nothing here but words."
        assert mask_emails(input_text) == input_text

    def test_email_with_numbers(self):
        """Tests email addresses with numbers."""
        assert mask_emails("user123@numbers.net") == "[EMAIL]"


# 7. Test for handling unexpected input (not needed for your function, but shows how to test exceptions)
def test_mask_emails_with_non_string():
    """Shows how to test for exceptions if non-string input is given."""
    with pytest.raises(TypeError):
        mask_emails(None)  # Should raise, since re.sub requires a string
