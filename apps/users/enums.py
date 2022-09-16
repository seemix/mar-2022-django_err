from enum import Enum


class RegEx(Enum):
    PASSWORD = (
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\s])([^\s]){8,30}$',
        [
            'password must contain number 0-9',
            'password must contain 1 uppercase symbol',
            'password must contain 1 lowercase symbol',
            'password must contain 1 non-alpha numeric',
            'password lenght 8-30 symbols without spaces'
        ]
    )
    NAME = (
        r'^[a-zA-Z]{2,25}',
        'only letters min 2 max 25'
    )

    PHONE = (
        r'^0[95678]{1}\d{8}',
        'bad phone format'
    )

    def __init__(self, pattern: str, message: str | list[str]):
        self.pattern = pattern
        self.message = message
