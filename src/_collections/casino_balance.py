from src.common.config import logger
from src.models.dict_entity import DictEntity


class CasinoBalances(DictEntity[str, int]):
    def print_rating(self):
        """
        Выводит отсортированную статистику объектов по их балансу.
        :return: Ничего не возвращает.
        """
        sorted_rating = sorted(self.data.items(), key=lambda item: -item[1])
        logger.info("Рейтинг казино:")
        for key, value in sorted_rating:
            if 'player' in key.lower() and value == 0:
                logger.info(f"{key}: остался у разбитого корыта без копеечки в кармане")
            else:
                logger.info(f"{key}: {value}")
