import base64
def encode(data: str) -> str:
    return   base64.b64encode(data.encode()).encode()
def decode(data: str) -> str:
    return    base64.b64decode(data.encode()).decode()