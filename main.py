

# Input variable where user must enter their email name

email = input("Enter your email: ")

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your user name is {username} and domain is {domain}")