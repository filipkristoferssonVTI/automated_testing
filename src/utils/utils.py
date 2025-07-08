import re


def mask_emails(text):
    """
    Replaces all email addresses in the input text with [EMAIL].
    """
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.sub(email_pattern, '[EMAIL]', text)
