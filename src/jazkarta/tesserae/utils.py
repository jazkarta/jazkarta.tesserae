"""Utility classes and functions"""

_marker = object()


class PrefixedFieldProperty(object):

    def __init__(self, field, prefix=''):
        self.field = field
        self.__name__ = field.__name__
        self.attribute_name = prefix + self.__name__

    def __get__(self, inst, klass):
        attribute = getattr(inst.context, self.attribute_name, _marker)
        if attribute is _marker:
            field = self.field.bind(inst)
            attribute = getattr(field, 'default', _marker)
            if attribute is _marker:
                raise AttributeError(self.__name__)
        return attribute

    def __set__(self, inst, value):
        field = self.field.bind(inst)
        field.validate(value)
        if field.readonly:
            raise ValueError(self.__name__, 'field is readonly')

        setattr(inst.context, self.attribute_name, value)
