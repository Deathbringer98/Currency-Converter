import requests

def get_exchange_rate(base_currency, target_currency):
    """
    Fetches the real-time exchange rate from the API and returns it.

    :param base_currency: str - the base currency code (e.g., "USD")
    :param target_currency: str - the target currency code (e.g., "EUR")
    :return: float - the exchange rate
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][target_currency]

def convert_currency(amount, base_currency, target_currency):
    """
    Converts a given amount from the base currency to the target currency.

    :param amount: float - the amount to convert
    :param base_currency: str - the base currency code
    :param target_currency: str - the target currency code
    :return: float - the converted amount
    """
    rate = get_exchange_rate(base_currency, target_currency)
    return amount * rate

# Example usage
amount = 100
base = "USD"
target = "EUR"
converted_amount = convert_currency(amount, base, target)
print(f"{amount} {base} is equal to {converted_amount:.2f} {target}")
