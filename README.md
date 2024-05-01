# Currency Converter

A simple Python utility that converts currency amounts from one currency to another using real-time exchange rates fetched from an API.

## Features

- Fetches real-time exchange rates.
- Converts amounts between a variety of currencies.

## Getting Started

### Prerequisites

This project requires Python and the `requests` library. Ensure you have Python installed, and install `requests` using pip:

```bash
pip install requests
```
Usage
The convert_currency function takes three parameters: the amount to convert, the base currency code, and the target currency code. Here's how to use it:
from currency_converter import convert_currency

# Example: Convert 100 USD to EUR
converted_amount = convert_currency(100, "USD", "EUR")
print(converted_amount)


Here's a Python program that demonstrates a practical application by implementing a basic currency converter. It uses real-time exchange rates by fetching data from an API. This example can showcase your ability to integrate APIs, handle data, and create functional tools in Python.

Python Program: Currency Converter
python
Copy code
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
README.md for Currency Converter
You should also include a README.md that describes your project, how to set it up, and how to use it. Here’s how you might write it:

markdown
Copy code
# Currency Converter

A simple Python utility that converts currency amounts from one currency to another using real-time exchange rates fetched from an API.

## Features

- Fetches real-time exchange rates.
- Converts amounts between a variety of currencies.

## Getting Started

### Prerequisites

This project requires Python and the `requests` library. Ensure you have Python installed, and install `requests` using pip:

```bash
pip install requests
```
Usage
The convert_currency function takes three parameters: the amount to convert, the base currency code, and the target currency code. Here's how to use it:

python
Copy code
from currency_converter import convert_currency

# Example: Convert 100 USD to EUR
converted_amount = convert_currency(100, "USD", "EUR")
print(converted_amount)
Contributing
Feel free to fork this project, make changes, and open a pull request to contribute. Your contributions are appreciated!
