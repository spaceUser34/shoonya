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

            buy_or_sell = 'B'
            product_type = 'C'
            exchange = 'NSE'
            tradingsymbol = 'INFY-EQ'
            quantity = '1000'
            discloseqty = '0'
            price_type = 'LMT'
            ltp_order1 = 303.0

            trigger_price = None
            retention = 'DAY'
            amo = None
            remarks = None
            bookloss_price = 0.0
            bookprofit_price = 0.0
            trail_price = 0.0

            rec_order_1 = self._shoonyaFinvasia.TransmitOrderToBrokerOMS(buy_or_sell, product_type, exchange,
                                                                         tradingsymbol, quantity, discloseqty, price_type, ltp_order1, trigger_price, retention, amo, remarks, bookloss_price, bookprofit_price, trail_price)
            if rec_order_1 != -1:
                print('Order ID: ', rec_order_1)
            else:
                print('order failed... in trading engine')

            buy_or_sell = 'S'
            product_type = 'C'
            price_type = 'LMT'
            ltp_order2 = 303.0

            rec_order_2 = self._shoonyaFinvasia.TransmitOrderToBrokerOMS(buy_or_sell, product_type, exchange,
                                                                         tradingsymbol, quantity, discloseqty, price_type, ltp_order2, trigger_price, retention, amo, remarks, bookloss_price, bookprofit_price, trail_price)
            if rec_order_2 != -1:
                print('Order ID: ', rec_order_2)
            else:
                print('order failed... in trading engine')

        except Exception as e:
            print('Error in Trasmitting the New Order: ', e)
