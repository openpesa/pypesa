"""Testing VodaCom M-Pesa Direct Debit Creation transaction

Testing common responses:
- successful transaction: status code 201
- duplicate transaction: status code 409
"""

from unittest.mock import patch

from pypesa.defaults import MPESA_API_KEY, MPESA_PUBLIC_KEY
from pypesa.vodacom import MPESA

from .samples import (duplicate_debit_creation_response,
                      successful_debit_creation_response)


class TestMpesaDirectDebitCreateTransaction:
    parameters = {
        "input_AgreedTC": "1",
        "input_Country": "TZN",
        "input_CustomerMSISDN": "000000000001",
        "input_EndRangeOfDays": "22",
        "input_ExpiryDate": "20211126",
        "input_FirstPaymentDate": "20160324",
        "input_Frequency": "06",
        "input_ServiceProviderCode": "000000",
        "input_StartRangeOfDays": "01",
        "input_ThirdPartyConversationID": "AAA6d1f9391a0052de0b5334a912jbsj1j2kk",
        "input_ThirdPartyReference": "3333"
    }

    @classmethod
    def setup(cls):
        cls.m_pesa = MPESA(api_key=MPESA_API_KEY, public_key=MPESA_PUBLIC_KEY)
        cls.mock_direct_debit_create_patcher = patch(
            'pypesa.vodacom.MPESA.direct_debit_create')
        cls.mock_direct_debit_create = \
            cls.mock_direct_debit_create_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_direct_debit_create_patcher.stop()

    def test_direct_debit_create_successful_transaction(self):
        """Test for successful direct_debit_create transaction
        Status code should be 201
        """
        self.mock_direct_debit_create.return_value.json.return_value = \
            successful_debit_creation_response

        response = self.m_pesa.direct_debit_create(self.parameters)

        assert self.mock_direct_debit_create.called
        assert response.json() == successful_debit_creation_response
        assert response.json()[0]['status_code'] == 201

    def test_direct_debit_create_duplicate_transaction(self):
        """Test for duplicate direct_debit_create transaction
        Status code should be 409
        """
        self.mock_direct_debit_create.return_value.json.return_value = \
            duplicate_debit_creation_response

        response = self.m_pesa.direct_debit_create(self.parameters)

        assert self.mock_direct_debit_create.called
        assert response.json() == duplicate_debit_creation_response
        assert response.json()[0]['status_code'] == 409
