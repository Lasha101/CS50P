import sys
import requests

def main():
    m = how_many_bitcoins()
    n = get_price_bitcoin()
    a = print_total_price(n, m)
    print(f"${a:,.4f}")

def how_many_bitcoins():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing comand-line argument")
        n = float(sys.argv[1])
        return n
    except ValueError:
        sys.exit("Comand-line argument is not a number")

def get_price_bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    try:
        response = requests.get(url)
        data = response.json()
        string_price = float(data['bpi']['USD']['rate_float'])
        float_price = string_price
        return float_price
    except requests.RequestException:
        sys.exit()

def print_total_price(n, m):
    amount = n * m
    return amount

if __name__ == "__main__":
    main()


