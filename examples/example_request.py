import json

from httpsuite import Request, ENCODE

# 1. Creates the body of the request.
body = json.dumps({"hello": "world"})

# 2. Creates an HTTP request.
request = Request(
    method="GET",
    target="/",
    protocol="HTTP/1.1",
    headers={
        "Host": "www.google.com",
        "Connection": "keep-alive",
        "Content-Length": len(body),
    },
    body=body,
)

# 3. Parses the equivalent request as the above.
request_parsed = request = Request.parse(
    (
        b"GET / HTTP/1.1\r\n"
        b"Host: www.google.com\r\n"
        b"Connection: keep-alive\r\n"
        b"Content-Length: %i\r\n"
        b"\r\n"
        b"%b"
    )
    % (len(body), body.encode(ENCODE))
)
