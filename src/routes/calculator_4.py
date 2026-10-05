from flask import Blueprint, jsonify, request

from src.calculators.calculator_4 import calculate_average
from src.errors.error_handler import validate_numbers_payload


calculator_4_bp = Blueprint("calculator_4", __name__)


@calculator_4_bp.route("/calculator_4", methods=["POST"])
def calculator_4():
    """
    Recebe uma lista de números e retorna a média aritmética.

    Returns:
        Resposta JSON contendo o resultado ou uma mensagem de erro.
    """
    body = request.get_json(silent=True)

    try:
        numbers = validate_numbers_payload(body)
        result = calculate_average(numbers)

        return jsonify({"average": result}), 200

    except ValueError as error:
        return jsonify({"error": str(error)}), 400