from jmbo.models import ModelBase


class IndexedModelBase(ModelBase):
    """Thin wrapper as hook for django-haystack's discovery of
    indexable models."""
    pass
