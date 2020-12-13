"""
vodacom.py
-----------
This module contains the class for all M-Pesa transactions.
"""

from .defaults import (MPESA_B2BPAYMENT_URL, MPESA_B2CPAYMENT_URL,
                       MPESA_BASE_URL, MPESA_C2BPAYMENT_URL,
                       MPESA_GET_SESSION_URL, MPESA_REVERSAL_URL,
                       MPESA_TRANSACTION_STATUS_URL)
from .open_api import APIContext, APIMethodType, APIRequest

BASE_URL = MPESA_BASE_URL
get_session_url = MPESA_GET_SESSION_URL
c2bPayment_url = MPESA_C2BPAYMENT_URL
reversal_url = MPESA_REVERSAL_URL
b2cPayment_url = MPESA_B2CPAYMENT_URL
b2bPayment_url = MPESA_B2BPAYMENT_URL
transaction_status_url = MPESA_TRANSACTION_STATUS_URL


class MPESA:

    def __init__(self, api_key: str, public_key: str,
                 ssl: bool = True) -> None:
        """Generate context required for making transaction

        :param api_key: API key for your application
        :type api_key: string
        :param public_key: Open API public key
        :type public_key: string
        :param ssl: Either to use ssl or not, defaults to True
        :type ssl: bool, optional
        """
        self.context = APIContext(
            api_key, public_key, ssl=ssl, address=BASE_URL, port=443)
        self.context.add_header('Origin', '*')

    def get_encrypted_api_key(self) -> str:
        """A function to return encrypted API key

        :return: Encrypted API key
        :rtype: str
        """
        return APIRequest(self.context).create_bearer_token()

    def get_session_id(self, path: str = get_session_url) -> str:
        """A function to generate valid Session ID needed to transact on M-Pesa
        using OpenAPI.

        :param path: url, defaults to get_session_url
        :type path: string, optional
        :raises Exception: When request fails, exception must be raised.
        :return: A valid Session ID
        :rtype: str
        """
        self.context.update({'method_type': APIMethodType.GET,
                             'path': path})

        response = None

        try:
            response = APIRequest(self.context).execute()
        except Exception as e:
            print('Call Failed: ', e)

        if response is None:
            raise Exception(
                'SessionKey call failed to get response. Please check.')
        else:
            return response.body['output_SessionID']

    def _get_api_response(self, context: dict) -> dict:
        """A function for getting results from API call.

        :param context: A dictionary containing all the necessary
        parameters for making API call.
        :type context: dict
        :raises Exception: Exception raised when API call fails.
        :return: Response from API call.
        :rtype: dict
        """
        response = None
        try:
            response = APIRequest(context).execute()
        except Exception as e:
            print('Call Failed: ', e)

        if response is None:
            raise Exception('API call failed to get result. Please check.')
        else:
            return response

    def customer2business(self, parameters: dict,
                          path: str = c2bPayment_url) -> dict:
        """A standard customer-to-business transaction

        :param parameters: A dictionary containing all necessary
        key value pairs.
        :type parameters: dict
        :param path: url for customer-to-business transaction,
        defaults to c2bPayment_url
        :type path: str, optional
        :return: Response from API call.
        :rtype: dict

        Example of parameters:

        parameters = {
            'input_Amount': 10,
            'input_Country': 'TZN',
            'input_Currency': 'TZS',
            'input_CustomerMSISDN': '000000000001',
            'input_ServiceProviderCode': '000000',
            'input_ThirdPartyConversationID':
                'asv02e5958774f7ba228d83d0d689761',
            'input_TransactionReference': 'T1234C',
            'input_PurchasedItemsDesc': 'Shoes',
        }
        """

        self.context.update({
            'api_key': self.get_session_id(),
            'method_type': APIMethodType.POST,
            'path': path,
            'parameters': {k: v for k, v in parameters.items()}
        })

        response = self._get_api_response(self.context)
        return response

    def reversal(self, reversal_parameters: dict,
                 path: str = reversal_url) -> dict:
        """Reverse a successful transaction.

        :param reversal_parameters: A dictionary containing all the
        necessary information for reversing transaction.
        :type reversal_parameters: dict
        :param path: url for reversing transaction, defaults to reversal_url
        :type path: str, optional
        :return: Dictionary of reversed transaction when successful.
        :rtype: dict

        Example of reversal_parameters:

        reversal_parameters = {
            'input_ReversalAmount': '25',
            'input_Country': 'TZN',
            'input_ServiceProviderCode': '000000',
            'input_ThirdPartyConversationID':
                'asv02e5958774f7ba228d83d0d689761',
            'input_TransactionID': '0000000000001',
        }
        """
        self.context.update({
            'api_key': self.get_session_id(),
            'method_type': APIMethodType.PUT,
            'path': path,
            'parameters': {k: v for k, v in reversal_parameters.items()}
        })

        response = self._get_api_response(self.context)
        return response

    def business2customer(self, parameters: dict,
                          path: str = b2cPayment_url) -> dict:
        """A standard customer-to-business transaction.

        :param parameters: Information required for successful transaction.
        :type parameters: dict
        :param path: url for business to customer payment,
        defaults to b2cPayment_url
        :type path: str, optional
        :return: Response from API call.
        :rtype: dict

        Example of paramters:

        parameters = {
            'input_Amount': '10',
            'input_Country': 'TZN',
            'input_Currency': 'TZS',
            'input_CustomerMSISDN': '000000000001',
            'input_ServiceProviderCode': '000000',
            'input_ThirdPartyConversationID':
            'asv02e5958774f7ba228d83d0d689761',
            'input_TransactionReference': 'T1234C',
            'input_PaymentItemsDesc': 'Salary payment',
        }
       """
        self.context.update({
            'api_key': self.get_session_id(),
            'method_type': APIMethodType.POST,
            'path': path,
            'parameters': {k: v for k, v in parameters.items()}
        })

        response = self._get_api_response(self.context)
        return response

    def business2business(self, parameters: dict,
                          path: str = b2bPayment_url) -> dict:
        """Business-to-business transactions (Single Stage).

        :param parameters: Information necessary for business-to-business
        transaction.
        :type parameters: dict
        :param path: url for business-to-business transaction,
        defaults to b2bPayment_url
        :type path: str, optional
        :return: Response from API call.
        :rtype: dict

        Example of parameters:

        parameters = {
            'input_Amount': '10',
            'input_Country': 'TZN',
            'input_Currency': 'TZS',
            'input_CustomerMSISDN': '000000000001',
            'input_ServiceProviderCode': '000000',
            'input_ThirdPartyConversationID':'asv02e5958774f7ba228d83d0d689761',
            'input_TransactionReference': 'T1234C',
            'input_PaymentItemsDesc': 'Salary payment',
            }
        """
        self.context.update({
            'api_key': self.get_session_id(),
            'method_type': APIMethodType.POST,
            'path': path,
            'parameters': {k: v for k, v in parameters.items()}
        })

        response = self._get_api_response(self.context)
        return response

    def status(self, parameters: dict,
               path: str = transaction_status_url) -> dict:
        """Query the status of the transaction that has been initiated.

        :param parameters: Information necessary for querying
        transaction status.
        :type parameters: dict
        :param path: url for querying transaction status,
        defaults to transaction_status_url
        :type path: str, optional
        :return: Response from API call.
        :rtype: dict

        Example of paramters:

        parameters = {
            'input_QueryReference': '000000000000000000001',
            'input_ServiceProviderCode': '000000',
            'input_ThirdPartyConversationID':'asv02e5958774f7ba228d83d0d689761',
            'input_Country': 'TZN',
        }
        """
        self.context.update({
            'api_key': self.get_session_id(),
            'method_type': APIMethodType.GET,
            'path': path,
            'parameters': {k: v for k, v in parameters.items()}
        })

        response = self._get_api_response(self.context)
        return response
