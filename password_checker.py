import string

def check_password_strength(password):
    # Tracking security metrics
    has_length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    # Calculate a score out of 5
    score = sum([has_length, has_upper, has_lower, has_digit, has_special])
    
    # Validation Logic
    if score == 5:
        return "Strong Security Password! 💪 ⭐⭐⭐⭐⭐"
    elif 3 <= score <= 4:
        return "Medium Security — Try adding special characters or numbers. ⚠️ ⭐⭐⭐"
    else:
        return "Weak Password — Vulnerable to cyber attacks! ❌ ⭐"

print("--- BCA Password Security Auditor Engine ---")
while True:
    user_input = input("\nEnter a password to test safety (or type 'exit'): ")
    if user_input.lower() == 'exit':
        print("Shutting down tracker. Stay safe!")
        break
        
    result = check_password_strength(user_input)
    print(f"Analysis Result: {result}")
