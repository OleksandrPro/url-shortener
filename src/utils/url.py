def make_url(host: str, path: str) -> str:
    host = host.strip("/")
    path = path.lstrip("/")

    return f"{host}/{path}"