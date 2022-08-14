import os
import importlib.metadata
from medsig.analysis import get_main_frequency


def string():
    result: str = "unknown (git checkout)"
    try:
        with open(os.path.dirname(__file__) + "/VERSION", "r", encoding="utf-8") as file:
            version = file.read().strip()
            result = version if version else result
    except Exception as ex:
        result = str(ex)
    return result


__version__ = importlib.metadata.version('med-signal')
