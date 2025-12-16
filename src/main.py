from src.simulation import run_simulation


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    run_simulation(seed=13121, steps=30)


if __name__ == "__main__":
    main()
