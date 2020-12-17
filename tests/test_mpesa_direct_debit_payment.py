"""Testing VodaCom M-Pesa Direct Debit Payment transaction

Testing common responses:
- successful transaction: status code 201
- duplicate transaction: status code 409
"""

from unittest.mock import patch

from pypesa.defaults import MPESA_API_KEY, MPESA_PUBLIC_KEY
from pypesa.vodacom import MPESA

from .samples import (duplicate_debit_payment_response,
                      successful_debit_payment_response)


class TestMpesaDirectDebitPaymentTransaction:
    parameters = {
        "input_Amount": "10",
        "input_Country": "TZN",
        "input_Currency": "TZS",
        "input_CustomerMSISDN": "000000000001",
        "input_ServiceProviderCode": "000000",
        "input_ThirdPartyConversationID": "AAA6d1f939c1005v2de053v4912jbasdj1j2kk",
        "input_ThirdPartyReference": "5db410b459bd433ca8e5"
    }

    @classmethod
    def setup(cls):
        cls.m_pesa = MPESA(api_key=MPESA_API_KEY, public_key=MPESA_PUBLIC_KEY)
        cls.mock_direct_debit_payment_patcher = patch(
            'pypesa.vodacom.MPESA.direct_debit_payment')
        cls.mock_direct_debit_payment = \
            cls.mock_direct_debit_payment_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_direct_debit_payment_patcher.stop()

    def test_direct_debit_payment_successful_transaction(self):
        """Test for successful direct_debit_payment transaction
        Status code should be 201
        """
        self.mock_direct_debit_payment.return_value.json.return_value = \
            successful_debit_payment_response

        response = self.m_pesa.direct_debit_payment(self.parameters)

        assert self.mock_direct_debit_payment.called
        assert response.json() == successful_debit_payment_response
        assert response.json()[0]['status_code'] == 201

    def test_direct_debit_payment_duplicate_transaction(self):
        """Test for duplicate direct_debit_payment transaction
        Status code should be 409
        """
        self.mock_direct_debit_payment.return_value.json.return_value = \
            duplicate_debit_payment_response

        response = self.m_pesa.direct_debit_payment(self.parameters)

        assert self.mock_direct_debit_payment.called
        assert response.json() == duplicate_debit_payment_response
        assert response.json()[0]['status_code'] == 409
