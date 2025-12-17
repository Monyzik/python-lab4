from src.common.exceptions import NotEnoughElementsException
from src.models.list_entity import ListEntity
from src.objects.chip import Chip


class ChipCollection(ListEntity[Chip]):
    expected_type = Chip

    def __add__(self, other) -> "ChipCollection":
        if isinstance(other, ChipCollection):
            return ChipCollection(self.data + other.data)
        if isinstance(other, int):
            self.append(Chip(other))
            return ChipCollection(self.data)
        if isinstance(other, Chip):
            self.append(other)
            return ChipCollection(self.data)
        raise TypeError

    def __sub__(self, other) -> "ChipCollection":
        if isinstance(other, ChipCollection) or isinstance(other, Chip):
            other = other.count
        if isinstance(other, int):
            while not self.is_empty() and self.back <= other:
                other -= self.pop().count
            if self.is_empty():
                raise NotEnoughElementsException(self.__sub__)
            self.back -= other
            return ChipCollection(self.data)
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, ChipCollection):
            return self.count == other.count
        raise TypeError

    def __lt__(self, other):
        if isinstance(other, ChipCollection):
            return self.count < other.count
        raise TypeError

    def __le__(self, other):
        if isinstance(other, ChipCollection):
            return self.count <= other.count
        raise TypeError

    @property
    def count(self) -> int:
        """
        :return: Возвращает сумму фишек.
        """
        result = 0
        for chip in self:
            result += chip.count
        return result
