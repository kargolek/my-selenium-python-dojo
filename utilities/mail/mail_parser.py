def parse_github_verification_code(body: str):
    return ''.join([n for n in body[body.find("Verification code:"):body.find("\r\n\r\nIf you")] if n.isdigit()])


