from cryptodwarf.exceptions import CryptoDwarfError


class CryptoDwarfHttpError(CryptoDwarfError):
	pass


class HTTP500(CryptoDwarfHttpError):
    """
    The Web server (running the Web Site) encountered an unexpected condition
    that prevented it from fulfilling the request by the client (e.g. your Web
    browser or our CheckUpDown robot) for access to the requested URL.
    """

    def __str__(self):
        return repr('500 Internal server error')


class HTTP400(CryptoDwarfHttpError):
    """
    Http400 Error Exception
    The server cannot or will not process the request due to
    an apparent client error e.g., malformed request syntax,
    invalid request message framing, or deceptive request routing).
    """

    def __str__(self):
        return repr('400  Bad Request')


class HTTP401(CryptoDwarfHttpError):
    """
    Http401 Error Exception
    Similar to 403 Forbidden, but specifically for use when authentication
    is required and has failed or has not yet been provided.
    The response must include a WWW-Authenticate header field containing
    a challenge applicable to the requested resource.
    """

    def __str__(self):
        return repr('401 Unauthorized')


class HTTP403(CryptoDwarfHttpError):
    """
    Http403 Error Exception
    The request was a valid request, but the server is refusing to respond to it.
    403 error semantically means "unauthorized", i.e. the user does not
    have the necessary permissions for the resource.
    """

    def __str__(self):
        return repr('403 Forbidden')


class HTTP404(CryptoDwarfHttpError):
    """
    Http404 Error Exception
    The requested resource could not be found but may be available in the future.
    Subsequent requests by the client are permissible.
    """
    def __str__(self):
        return repr('404 not Found occurred')


class HTTP405(CryptoDwarfHttpError):
    """
    Http405 Error Exception
    A request method is not supported for the requested resource; for example,
    a GET request on a form which requires data to be presented via POST, or a
    PUT request on a read-only resource.
    """
    def __str__(self):
        return repr('405 Method Not Allowed')


class HTTP429(CryptoDwarfHttpError):
    """
    Http429 Error Exception
    The user has sent too many requests in a given amount of time.
    Intended for use with rate limiting schemes.
    """
    def __str__(self):
        return repr('429 Too Many Requests')


class HTTP503(CryptoDwarfHttpError):
    """
    Http503 Error Exception
    The server is currently unavailable (because it is overloaded or
    down for maintenance). Generally, this is a temporary state.
    """
    def __str__(self):
        return repr('503 Service Unavailable')
