import re

def validate_email(email: str) -> bool:
    """Validate email using regex."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.fullmatch(pattern, email))

def validate_bangladesh_mobile(number: str) -> bool:
    """Validate Bangladesh mobile number (supports +880, 880, 0 formats)."""
    pattern = r"^(?:\+880|880|0)(1[3-9])[0-9]{8}$"
    return bool(re.fullmatch(pattern, number))

def validate_usa_telephone(phone: str) -> bool:
    """Validate USA phone number formats like +1-123-456-7890, (123) 456-7890."""
    pattern = r"^(?:\+1[-.\s]?)?\(?([2-9][0-9]{2})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})$"
    return bool(re.fullmatch(pattern, phone))

def validate_secure_password(password: str) -> bool:
    """Validate 16-character alphanumeric password with special characters."""
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$"
    return bool(re.fullmatch(pattern, password))

# Test Cases
test_cases = {
    "email": "example@email.com",
    "bangladesh_mobile": "+8801712345678",
    "usa_telephone": "+1-123-456-7890",
    "secure_password": "Aa1@Bb2#Cc3$Dd4!"  # 16-char secure password
}

# Validation Results
print(f"Email Validation: {validate_email(test_cases['email'])}")
print(f"Bangladesh Mobile Validation: {validate_bangladesh_mobile(test_cases['bangladesh_mobile'])}")
print(f"USA Telephone Validation: {validate_usa_telephone(test_cases['usa_telephone'])}")
print(f"Secure Password Validation: {validate_secure_password(test_cases['secure_password'])}")
