# grading_system.py

# We assume the user enters a valid number for simplicity here.
score = int(input("Enter the score (0-100): "))

if score < 0 or score > 100: # Check for invalid input first using 'or'
    print("Invalid score entered.")
elif score >= 70:
    print("Grade: Distinction")
elif score >= 60:
    print("Grade: Merit")
elif score >= 50:
    print("Grade: Pass")
else: # Only remaining possibility is score < 50
    print("Grade: Fail")

print("Grading complete.")