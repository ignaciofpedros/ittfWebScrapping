from src.clean_scrapping.domain import match as ma
from src.clean_scrapping.domain import player as pl

class MemRepo:

    def __init__(self, entries=None):
        self._entries = []
        if entries:
            self._entries.extend(entries)

    def _check(self, element, key, value):
        if '__' not in key:
            key = key + '__eq'

        key, operator = key.split('__')

        if operator not in ['eq', 'lt', 'gt']:
            raise ValueError('Operator {} is not supported'.format(operator))

        operator = '__{}__'.format(operator)

        if key in ['year']:
            return getattr(element[key], operator)(int(value))
        elif key in ['tournament', 'score']:
            return getattr(element[key], operator)(str(value))
        elif key in ['player1', 'player2', 'winner']:
            return getattr(element[key], operator)(pl(value))

        return getattr(element[key], operator)(value)

    def list(self, filters=None):
        if not filters:
            result = self._entries
        else:
            result = []
            result.extend(self._entries)

            for key, value in filters.items():
                result = [e for e in result if self._check(e, key, value)]

        return [ma.Match.from_dict(r) for r in result]
