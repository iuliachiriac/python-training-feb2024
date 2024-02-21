class InvalidDomain(Exception):
    pass


def parse_email(email_address):
    username, domain = email_address.split("@")
    if "." not in domain:
        raise InvalidDomain(f"{domain} does not look like a valid domain.")
    return username, domain


email_addresses = [
    "admin@site.com",
    "admin@site",
    "test",
    "@@gmail.com",
    "ana@gmail.com",
]
for email in email_addresses:
    try:
        user, dom = parse_email(email)
    except ValueError:
        print(f"Invalid email address: {email}")
    except InvalidDomain as ex:
        print(ex)
    else:
        print(f"{user} registered on {dom}")
    finally:
        print(f"Done for {email}.\n")
