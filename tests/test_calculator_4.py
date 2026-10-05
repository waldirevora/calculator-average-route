from src.calculators.calculator_4 import calculate_average


def test_calculate_average():
    """
    Verifica se a média de uma lista de números é calculada corretamente.
    """
    numbers = [10, 20, 30]

    result = calculate_average(numbers)

    assert result == 20