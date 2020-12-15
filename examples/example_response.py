import json

from httpsuite import Response, ENCODE

# 1. Creates the body of the request.
body = json.dumps({"hello": "world"})

# 2. Creates an HTTP response.
response = Response(
    protocol="HTTP/1.1",
    status=200,
    status_msg="OK",
    headers={
        "Host": "www.google.com",
        "Connection": "keep-alive",
        "Content-Length": len(body),
    },
    body=body,
)

# 3. Parses the equivalent response as the above.
response_parsed = Response.parse(
    (
        b"HTTP/1.1 200 OK\r\n"
        b"Host: www.google.com\r\n"
        b"Connection: keep-alive\r\n"
        b"Content-Length: %i\r\n"
        b"\r\n"
        b"%b"
    )
    % (len(body), body.encode(ENCODE))
)
