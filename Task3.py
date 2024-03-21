#Task no 3 Prajwal Kunjekar
import re
import sys

def assess_password_strength(password):
    # Checking criteria
    has_numbers = any(char.isdigit() for char in password)
    has_upper_lower_case = any(char.isupper() or char.islower() for char in password)
    meets_length_requirement = len(password) >= 8
    has_special_characters = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Counts the number of met criteria
    met_criteria_count = sum([has_numbers, has_upper_lower_case, meets_length_requirement, has_special_characters])

    # Classifies the password based on the number of met criteria
    if met_criteria_count == 4:
        return "Password Strength Level: Very Strong (All criteria are met)."
    elif met_criteria_count == 3:
        return "Password Strength Level: Moderately Strong (Any 3 criteria are met)."
    elif met_criteria_count == 2:
        return "Password Strength Level: Strong (Any 2 criteria are met)."
    else:
        return "Password Strength Level: Weak (None or only one criterion is met)."

def main():
    print("---------------- Password Strength Checker -----------------")

    password_input = input("Enter your password: ")

    # Assesses the password strength
    result = assess_password_strength(password_input)

    # Provides more specific feedback to the user
    print("\n{}".format(result))
    print("\nHere are some quick tips for creating a secure password:")
    print("1. Length: Aim for at least 12 characters.")
    print("2. Mix Characters: Use a combination of uppercase, lowercase, numbers, and symbols.")
    print("3. Avoid Common Words: Don't use easily guessable information.")
    print("4. No Personal Info: Avoid using names, birthdays, or personal details.")
    print("5. Use Passphrases: Consider combining multiple words or a sentence.")
    print("6. Unique for Each Account: Don't reuse passwords across multiple accounts.")
    print("7. Regular Updates: Change passwords periodically.")
    print("8. Enable 2FA: Use Two-Factor Authentication where possible.")
    print("9. Be Wary of Phishing: Avoid entering passwords on suspicious sites.")
    print("10. Password Manager: Consider using one for secure and unique passwords.")

if __name__ == "__main__":
    main()
