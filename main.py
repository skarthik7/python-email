# GUI
# which email service do you use

from email_validator import validate_email, EmailNotValidError

email = "karthikakella@kockw.com"

try:
  # Validate & take the normalized form of the email
  # address for all logic beyond this point (especially
  # before going to a database query where equality
  # does not take into account normalization).
  email = validate_email(email).email
except EmailNotValidError as e:
  # email is not valid, exception message is human-readable
  print(str(e))