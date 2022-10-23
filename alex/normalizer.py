from urllib.parse import urlparse, ParseResult


def normalize(s: str) -> str:
    parsed_uri = urlparse(s.strip())
    scheme = 'http' if not parsed_uri.scheme else parsed_uri.scheme
    netloc, path = [parsed_uri.path, ''] if parsed_uri.netloc == '' and parsed_uri.path else [parsed_uri.netloc, parsed_uri.path]
    if not netloc:
        netloc = 'localhost'
    if len(netloc.split(':')) < 2:
        netloc = netloc + ':80'
    if not path:
        path = '/'
    new_uri = ParseResult(scheme=scheme, netloc=netloc, path=path, params=parsed_uri.params,
                          query=parsed_uri.query, fragment=parsed_uri.fragment)
    return new_uri.geturl()
