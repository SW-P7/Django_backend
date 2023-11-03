


def register_viewset(router, prefix, basename=None):
    """
    Decorator to register a viewset with a router.
    
    :router: Default router in views file
    :param prefix: URL prefix for the viewset
    :param basename: Base name to use for the URL names that are created
    """
    def decorator(viewset_cls):
        router.register(prefix, viewset_cls, basename=basename if basename else viewset_cls.__name__.lower())
        return viewset_cls
    return decorator
