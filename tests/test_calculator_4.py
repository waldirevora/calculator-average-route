from app import app
from src.calculators.calculator_4 import calculate_average


def test_calculate_average():
    """
    Verifica se a média de uma lista de números é calculada corretamente.
    """
    numbers = [10, 20, 30]

    result = calculate_average(numbers)

    assert result == 20


def test_calculator_4_route():
    """
    Verifica se a rota retorna a média correta para uma requisição válida.
    """
    client = app.test_client()

    response = client.post(
        "/calculator_4",
        json={"numbers": [10, 20, 30]},
    )

    data = response.get_json()

    assert response.status_code == 200
    assert data["average"] == 20


def test_calculator_4_route_without_numbers():
    """
    Verifica se a rota rejeita uma requisição sem o campo numbers.
    """
    client = app.test_client()

    response = client.post(
        "/calculator_4",
        json={"values": [10, 20, 30]},
    )

    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] == "O campo 'numbers' é obrigatório."

def test_calculator_4_route_with_empty_list():
    """
    Verifica se a rota rejeita uma lista vazia.
    """
    client = app.test_client()

    response = client.post(
        "/calculator_4",
        json={"numbers": []},
    )

    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] == "O campo 'numbers' deve ser uma lista não vazia."


def test_calculator_4_route_with_non_numeric_value():
    """
    Verifica se a rota rejeita valores que não sejam numéricos.
    """
    client = app.test_client()

    response = client.post(
        "/calculator_4",
        json={"numbers": [10, "20", 30]},
    )

    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] == "Todos os valores de 'numbers' devem ser numéricos."