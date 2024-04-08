import threading


class ExchangeRate:

    def __init__(self, base_currency, target_currency, rate):
        self.target_currency = target_currency
        self.base_currency = base_currency
        self.rate = rate

class Convertor:
    _instance = None
    _lock: threading.Lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            cls._instance._exchange_rate = []
        return cls._instance

    def loadExchangeRate(self):
        er = ExchangeRate("USD", "JPY", 0.1)
        er2 = ExchangeRate("SAR", "EGP", 0.816)
        er3 = ExchangeRate("USD", "EUR", 0.9)
        self._exchange_rate.extend([er, er2, er3])

    def convert(self, from_currency, to_currency, amount):
        for er in self._exchange_rate:
            if er.base_currency == from_currency and er.target_currency == to_currency:
                return er.rate * amount
        return None


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
