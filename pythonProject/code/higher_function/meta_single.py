# -*-coding:utf-8-*-
import threading


class singleMeta(type):
    """自定义元类"""

    def __init__(cls, *args, **kwargs):
        cls._instance = None
        cls._lock = threading.RLock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__call__(*args, *kwargs)
        return cls._instance


class President(metaclass=singleMeta):
    pass
