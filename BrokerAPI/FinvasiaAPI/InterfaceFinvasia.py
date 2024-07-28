from BrokerAPI.FinvasiaAPI.api_helper import ShoonyaApiPy
from CredentialsTo.CredentialsToBroker import CredentialsToFinvasia
import pyotp
import datetime


class InterfaceFinvasia:
    def __init__(self):
        self._shoonyaAPI = ShoonyaApiPy()
        self._isConnected = False

    def LoginPanel(self):
        print("Inside Login Panel...")
        totp = pyotp.TOTP(CredentialsToFinvasia.AUTHKEY).now()
        ret = self._shoonyaAPI.login(
            userid=CredentialsToFinvasia.Uid,
            password=CredentialsToFinvasia.Password,
            twoFA=totp,
            vendor_code=CredentialsToFinvasia.VendorCode,
            api_secret=CredentialsToFinvasia.APIKEY,
            imei=CredentialsToFinvasia.IMEI,
        )
        print("Login Panel: ", ret['stat'])
        if ret['stat'] == 'Ok':
            self._isConnected = True
            print('Successfuly Connected')
        else:
            print('Connection Failed...')

    def isConnected(self):
        return self._isConnected

    def RequestToBroker(self):
        if not self._isConnected:
            print('Please Connect To Broker')
            return
        print('Getting Historical Data...')
        previous_date = datetime.datetime.today() - datetime.timedelta(days=2)
        uxEntryTime = int(previous_date.timestamp())

        # ohlc = self._shoonyaAPI.get_time_price_series(
        #     exchange='NSE', token='26000', starttime=str(uxEntryTime), endtime=None)
        # print(ohlc)

    def CloseAPI(self):
        try:
            if not self._isConnected:
                print("connection Already Closed")
                return

            result = self._shoonyaAPI.logout()
            print(f'Logout result : {result}')

        except Exception as e:
            print('logout failed with error', e)

    def TransmitOrderToBrokerOMS(self):
        try:
            print('sending Trades...')
            ord_msg = self._shoonyaAPI.place_order(
                'B', 'C', 'NSE', 'TATACOMM-EQ', '1000', '0', 'MKT')

            print('Order :', ord_msg)
        except Exception as e:
            print('Error in placing order: ', e)
