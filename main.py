# GUI
# which email service do you use

from email_validator import validate_email, EmailNotValidError


def validate(email):
    try:
        email = validate_email(email).email
        valid = True
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        print(str(e))
        valid = False
    
    return valid

def getService(email):
    start = email.find("@") + len("@")
    end = email.find(".")
    substring = email[start:end]
    print(substring)

def main():
    email = "test@ing.com"
    if validate(email) == True:
        service = getService(email)
        print(service)
    else:
        pass