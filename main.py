from convertor import Convertor

if __name__ == "__main__":
    convertor = Convertor()
    convertor.loadExchangeRate()
    convertor2 = Convertor()
    convertor2.loadExchangeRate()

    while True:
        base_currency = input("Enter base currency: ")
        target_currency = input("Enter target currency: ")
        amount = float(input("Enter amount: "))

        result = convertor.convert(base_currency, target_currency, amount)
        result2 = convertor.convert(base_currency, target_currency, amount)

        print(result)
        print(result2)

