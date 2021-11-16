import uuid


def generate_random_string(length=10, upper_case=False):
    result = str(uuid.uuid4())
    if upper_case:
        result = result.upper()
    result = result.replace("-", "")
    return result[0:length]
