from clients import CoinConversorService


client = CoinConversorService()
conversion = client.converter("BTC", "USD")

print(f"R$ {conversion}")
