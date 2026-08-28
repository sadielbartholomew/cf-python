class UMArray:
    """A UM array."""

    def __init__(self, *args, **kwargs):
        class DeprecationError(Exception):
            """Deprecation error."""

        raise DeprecationError(
            f"{self.__class__.__name__} was deprecated at version 3.21.0 "
            "and is no longer available. Use XnetcdfArray instead."
        )
