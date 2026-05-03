# Mimics Amazon Comprehend for PII and AWS IAM for permissions.

import re

def redact_pii(text: str):
    """Simple regex to mimic PII redaction (Emails/Phones)"""
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    redacted = re.sub(email_pattern, "[REDACTED_EMAIL]", text)
    return redacted

def check_permission(action: str):
    """Mimics a policy check (IAM)"""
    prohibited_actions = ["delete", "remove", "wipe", "fire"]
    
    if any(word in action.lower() for word in prohibited_actions):
        return False
    return True