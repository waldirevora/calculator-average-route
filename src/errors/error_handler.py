def validate_numbers_payload(body):
    """
    Valida os dados recebidos pela rota da calculadora.

    Args:
        body: Corpo JSON recebido na requisição.

    Returns:
        Lista de números validada.

    Raises:
        ValueError: Quando os dados enviados estão em formato inválido.
    """
    if not isinstance(body, dict) or "numbers" not in body:
        raise ValueError("O campo 'numbers' é obrigatório.")

    numbers = body["numbers"]

    if not isinstance(numbers, list) or not numbers:
        raise ValueError("O campo 'numbers' deve ser uma lista não vazia.")

    if not all(
        isinstance(number, (int, float)) and not isinstance(number, bool)
        for number in numbers
    ):
        raise ValueError("Todos os valores de 'numbers' devem ser numéricos.")

    return numbers