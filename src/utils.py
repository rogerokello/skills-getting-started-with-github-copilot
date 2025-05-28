import html
import re

def sanitize_html(text):
    """Sanitize text to prevent XSS attacks."""
    if not isinstance(text, str):
        return text
    return html.escape(text, quote=True)

def sanitize_email(email):
    """Sanitize and validate email address."""
    if not isinstance(email, str):
        raise ValueError("Email must be a string")
    # Basic email validation and sanitization
    email = email.strip().lower()
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        raise ValueError("Invalid email format")
    return sanitize_html(email)
