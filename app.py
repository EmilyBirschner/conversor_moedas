from flask import Flask, render_template, request
from clients import CoinConversorService

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None
    moeda_origem_val = ""
    moeda_destino_val = ""
    valor_val = 1.0

    if request.method == "POST":
        try:
            # Captura os dados do formulário
            moeda_origem_val = request.form.get("moeda_origem", "").upper().strip()
            moeda_destino_val = request.form.get("moeda_destino", "").upper().strip()
            valor_val = float(request.form.get("valor"))

            # Chama lógica de conversão
            client = CoinConversorService()
            cotacao = client.converter(moeda_origem_val, moeda_destino_val)

            if cotacao:
                valor_final = float(cotacao) * valor_val
                resultado = f"{moeda_destino_val} {valor_final:,.2f}"
            else:
                erro = "Não foi possível obter a cotação. Verifique os códigos (Ex: BTC, USD)."

        except ValueError:
            erro = "Por favor, insira um valor numérico válido."
        except Exception as e:
            erro = f"Erro ao processar: {str(e)}"

    return render_template(
        "index.html",
        resultado=resultado,
        erro=erro,
        v_origem=moeda_origem_val,
        v_destino=moeda_destino_val,
        v_valor=valor_val,
    )


if __name__ == "__main__":
    app.run()
