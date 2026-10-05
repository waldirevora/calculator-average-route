from flask import Flask

from src.routes.calculator_4 import calculator_4_bp


app = Flask(__name__)

app.register_blueprint(calculator_4_bp)


if __name__ == "__main__":
    app.run(debug=True)