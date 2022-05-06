# GUI
# which email service do you use

from email_validator import validate_email, EmailNotValidError
import smtplib, ssl

def validate(email):
  try:
    email = validate_email(email).email
    valid = True
  except EmailNotValidError as e: 
    print(str(e))
    valid = False
    
  return valid

def getService(email):
  start = email.find("@") + len("@")
  if email.count(".") == 1:
    end = email.find(".")
  else:
    end = email.find('.', email.find('.') + 1)
  substring = email[start:end]
  return substring

def main():
 
  email = "skakella7@gmail.com"
  if validate(email) == True:
    service = getService(email)
    print(service)
  else:
      pass
main()
