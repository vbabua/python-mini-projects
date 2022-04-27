email = input("Enter the email address : ").strip()
username = email[ : email.index("@")]
domain = email[email.index("@") + 1 :]
print(f"Username is '{username}' and domain is '{domain}'")