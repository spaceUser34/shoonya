import TradingEngine as te

if __name__ == "__main__":
    handler = te.TradingEngine()
    handler.ConnectToBroker()
    handler.StartEngine()
