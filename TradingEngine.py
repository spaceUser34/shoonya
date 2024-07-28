from BrokerAPI.FinvasiaAPI import InterfaceFinvasia


class TradingEngine:
    def __init__(self):
        print("::::::::-Welcome to Trading Engine-::::::::")
        self._shoonyaFinvasia = InterfaceFinvasia.InterfaceFinvasia()

    def ConnectToBroker(self):
        try:
            self._shoonyaFinvasia.LoginPanel()
        except Exception as e:
            print("Connection To Broker Error: ", e)

    def StartEngine(self):
        if self._shoonyaFinvasia.isConnected():
            self._shoonyaFinvasia.RequestToBroker()
            self.TakeNewEntry()
        else:
            print('Requesting Failed...')

        self._shoonyaFinvasia.CloseAPI()

    def TakeNewEntry(self):
        try:
            print('Taking New Entry...')
            self._shoonyaFinvasia.TransmitOrderToBrokerOMS()
        except Exception as e:
            print('Error in Trasmitting the New Order: ', e)
