import os

# Get secret from environment variable
pam_secret = os.getenv("PAM_SECRET")

if pam_secret:
    print("Access granted with secret:", pam_secret)
else:
    print("No secret found. Access denied.")
