from src.common.exceptions import NegativeArgumentException
from src.simulation import run_simulation


def main() -> None:
    """
    Пользователь вводит число шагов и сид, с которым будет запущенна симуляция.
    :return: Данная функция ничего не возвращает
    """
    try:
        steps = int(input("Введите количество шагов симуляции: "))
    except ValueError:
        print("Значение должно быть целым числом")
        return
    try:
        seed = input("Введите сид, либо 'None' при его отсутствии: ")
        if seed == "None":
            seed = None
        else:
            seed = int(seed)
    except ValueError:
        print("Значение должно быть целым числом")
        return
    try:
        run_simulation(steps=steps, seed=seed)
    except NegativeArgumentException:
        print("Значение должно быть неотрицательным числом")
        return


if __name__ == "__main__":
    main()
