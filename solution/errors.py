"""Structured error type carrying a locatable code and field path."""


class SolutionError(Exception):
    """An error that must be reported to the caller as structured JSON.

    Attributes:
        code: machine-readable error code (e.g. "SCHEMA_MISSING").
        message: human-readable explanation.
        path: location of the offending field, e.g.
            "applications[0].materials[1].required".  Empty string means
            the error concerns the request as a whole.
    """

    def __init__(self, code, message, path=""):
        super().__init__("%s: %s (at %s)" % (code, message, path or "<root>"))
        self.code = code
        self.message = message
        self.path = path

    def to_dict(self):
        return {
            "status": "error",
            "error": {
                "code": self.code,
                "path": self.path,
                "message": self.message,
            },
        }
