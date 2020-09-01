import json
from itertools import chain
from typing import Union

# https://stackoverflow.com/questions/3387691/how-to-perfectly-override-a-dict


class JsonMsgDict(dict):
    # dicts take a mapping or iterable as their optional first argument
    type: str
    content: str
    author: str
    task: Union[str, None]

    @staticmethod
    def _process_args(mapping=(), **kwargs):
        include = ['type', 'content', 'author']
        if hasattr(mapping, "items"):
            mapping = getattr(mapping, "items")()

        if not all(list(map(lambda x: x in [k for k, _ in mapping], include))):
            raise NotImplementedError

        return ((k, v) for k, v in chain(mapping, getattr(kwargs, 'items')()))

    def __init__(self, mapping=(), **kwargs):
        super(JsonMsgDict, self).__init__(
            self._process_args(mapping, **kwargs))

    def copy(self):  # don't delegate w/ super - dict.copy() -> dict :(
        return type(self)(self)

    def __repr__(self):
        return '{0}({1})'.format(type(self).__name__, super(JsonMsgDict, self).__repr__())

    def __str__(self) -> str:
        return json.dumps(super(JsonMsgDict, self).__repr__())
