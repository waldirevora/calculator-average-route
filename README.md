# Calculadora: Rota de Média (Calculator Average Route)

API desenvolvida em Python com Flask para calcular a média aritmética de uma lista de números.

O projeto foi desenvolvido como desafio prático da Rocketseat, com foco em organização do código, separação de responsabilidades, validação de dados e testes automatizados.

## Objetivo

Criar uma rota `POST /calculator_4` capaz de receber uma lista de números em formato JSON, calcular a média aritmética e retornar o resultado.

A aplicação também trata entradas inválidas e retorna respostas adequadas quando os dados enviados não seguem o formato esperado.

## Tecnologias

1. Python 3.14.7
2. Flask 3.1.3
3. pytest 9.1.1
4. Git
5. GitHub

## Funcionalidades

1. Recebimento de uma lista de números por requisição HTTP POST
2. Cálculo da média aritmética
3. Retorno do resultado em JSON
4. Validação do corpo da requisição
5. Validação da existência do campo `numbers`
6. Validação de lista vazia
7. Validação de valores não numéricos
8. Tratamento de JSON inválido
9. Respostas HTTP adequadas para sucesso e erro
10. Testes automatizados da lógica e da rota

## Estrutura do projeto

```text
calculator-average-route

app.py
requirements.txt
README.md
.gitignore

src
    calculators
        calculator_4.py

    errors
        error_handler.py

    routes
        calculator_4.py

tests
    test_calculator_4.py
```

## Responsabilidades

### app.py

Inicializa a aplicação Flask e registra a rota da calculadora.

### src/calculators/calculator_4.py

Contém a função responsável pelo cálculo da média aritmética.

### src/routes/calculator_4.py

Define a rota `POST /calculator_4` e controla a entrada e a saída HTTP.

### src/errors/error_handler.py

Valida os dados recebidos pela API antes da execução do cálculo.

### tests/test_calculator_4.py

Contém os testes automatizados da função de cálculo, da rota e dos cenários de erro.

## Pré requisitos

É necessário ter Python instalado no computador.

A versão utilizada durante o desenvolvimento foi:

```text
Python 3.14.7
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/waldirevora/calculator-average-route.git
```

Entre na pasta:

```bash
cd calculator-average-route
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

No Windows PowerShell, ative o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executando a aplicação

Com o ambiente virtual ativo:

```bash
python app.py
```

A aplicação será iniciada em:

```text
http://127.0.0.1:5000
```

## Endpoint

### POST /calculator_4

Recebe uma lista de números e retorna a média aritmética.

Exemplo de requisição:

```json
{
  "numbers": [10, 20, 30]
}
```

Exemplo de resposta:

```json
{
  "average": 20.0
}
```

## Testando pelo PowerShell

Com a aplicação executando, abra outro terminal e utilize:

```powershell
Invoke-RestMethod `
    -Uri "http://127.0.0.1:5000/calculator_4" `
    -Method Post `
    -ContentType "application/json" `
    -Body '{"numbers":[10,20,30]}'
```

Resposta esperada:

```text
average
20.0
```

## Tratamento de erros

Quando o campo `numbers` não é enviado:

```json
{
  "values": [10, 20, 30]
}
```

A API retorna HTTP `400` com uma mensagem informando que o campo é obrigatório.

A aplicação também rejeita:

1. Lista vazia
2. Valores não numéricos
3. JSON inválido
4. Corpo sem o campo `numbers`

## Testes

Os testes podem ser executados com:

```bash
python -m pytest
```

Durante a validação do projeto foram implementados seis testes.

Eles verificam:

1. Cálculo correto da média
2. Funcionamento da rota com dados válidos
3. Requisição sem o campo `numbers`
4. Lista vazia
5. Valor não numérico
6. JSON inválido

Resultado esperado:

```text
6 passed
```

## Organização do código

A lógica de cálculo foi mantida separada da camada HTTP.

A rota recebe a requisição e utiliza a função responsável pelo cálculo.

A validação dos dados também possui responsabilidade própria, evitando que a função de cálculo precise conhecer detalhes da requisição HTTP.

Essa organização facilita testes, manutenção e leitura do código sem adicionar complexidade desnecessária ao projeto.

## Status

Projeto concluído e testado.

## Autor

Waldir Évora

GitHub:

https://github.com/waldirevora

## Repositório

https://github.com/waldirevora/calculator-average-route
