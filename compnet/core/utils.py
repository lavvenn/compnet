__all__ = ()

import re


def normalize_name(name: str) -> str:
    normalize_dict = {
        'a': 'а',
        'e': 'е',
        'ё': 'е',
        'c': 'с',
        'p': 'р',
        'o': 'о',
        'x': 'х',
        'y': 'у',
        't': 'т',
        'b': 'в',
        'm': 'м',
        'h': 'н',
        'k': 'к',
        'й': 'и',
    }

    replaced_chars = ''.join(normalize_dict.get(ch, ch) for ch in name.lower())

    return re.sub(r'[^а-я0-9]', '', replaced_chars, flags=re.UNICODE)
