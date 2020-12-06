"""Test suite for testing VodaCom M-Pesa customer-to-business transaction
Testing common responses:
- successful transaction: status code 201
- duplicate transaction: status code 409
"""

from unittest.mock import patch

from pypesa.defaults import *
from pypesa.vodacom import MPESA


def test_get_encrypted_api_key_method():
    m_pesa = MPESA(api_key=MPESA_API_KEY, public_key=MPESA_PUBLIC_KEY)

    enc_key = m_pesa.get_encrypted_api_key()

    assert enc_key is not None


@patch('pypesa.vodacom.MPESA.get_session_id')
def test_get_session_id_method(mock_get_session_id):
    mock_get_session_id.return_value = 'f34ba72a7ee94e9a85f9c0087b5f8d5b'

    m_pesa = MPESA(api_key=MPESA_API_KEY, public_key=MPESA_PUBLIC_KEY)

    session_id = m_pesa.get_session_id()

    assert mock_get_session_id.called
    assert session_id == 'f34ba72a7ee94e9a85f9c0087b5f8d5b'


class TestMpesaCustome2BusinessTransaction:
    @classmethod
    def setup(cls):
        cls.m_pesa = MPESA(api_key=MPESA_API_KEY, public_key=MPESA_PUBLIC_KEY)
        cls.mock_customer2business_patcher = patch(
            'pypesa.vodacom.MPESA.customer2business')
        cls.mock_customer2business = cls.mock_customer2business_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_customer2business_patcher.stop()

    def test_customer2business_successful_transaction(self):
        """Test for successful customer2business transaction
        Status code should be 201
        """
        successful_transaction_sample = [{
            'status_code': 201,
            'headers': {'date': 'Sun, 06 Dec 2020 05:11:43 GMT',
                        'x-frame-options': 'SAMEORIGIN', 'x-robots-tag': 'none',
                        'x-content-type-options': 'nosniff',
                        'x-xss-protection': '1; mode=block',
                        'strict-transport-security': 'max-age=16005600; includeSubDomains',
                        'content-type': 'application/json',
                        'access-control-allow-origin': '*',
                        'content-length': '252', 'Vary': 'Accept-Encoding'},
            'body': {'output_ResponseCode': 'INS-0',
                    'output_ResponseDesc': 'Request processed successfully',
                    'output_TransactionID': 'G27DEn1DLoQ3',
                    'output_ConversationID': '08536a5d65ea4f50866db06f577cc5c1',
                    'output_ThirdPartyConversationID': 'asv02e5958774f7ba228d83d0d689761'}
        }]

        self.mock_customer2business.return_value.json.return_value = \
            successful_transaction_sample

        parameters = {
            'input_Amount': 10,
            'input_Country': 'TZN',
            'input_Currency': 'TZS',
            'input_CustomerMSISDN': '000000000001',
            'input_ServiceProviderCode': '000000',
            'input_ThirdPartyConversationID': 'asv02e5958774f7ba228d83d0d689761',
            'input_TransactionReference': 'T1234C',
            'input_PurchasedItemsDesc': 'Shoes',
        }

        response = self.m_pesa.customer2business(parameters)

        assert self.mock_customer2business.called
        assert response.json() == successful_transaction_sample
        assert response.json()[0]['status_code'] == 201

    def test_customer2business_duplicate_transaction(self):
        """Test for duplicate customer2business transaction
        Status code should be 409
        """
        duplicate_transaction_sample = [{
            'status_code': 409,
            'headers': {'date': 'Sun, 06 Dec 2020 05:12:04 GMT',
                        'x-frame-options': 'SAMEORIGIN', 'x-robots-tag': 'none', 'x-content-type-options': 'nosniff',
                        'x-xss-protection': '1; mode=block', 'strict-transport-security': 'max-age=16005600; includeSubDomains',
                        'content-type': 'application/json',
                        'access-control-allow-origin': '*', 'content-length': '235', 'Vary': 'Accept-Encoding'},
            'body': {'output_ResponseCode': 'INS-10',
                    'output_ResponseDesc': 'Duplicate Transaction',
                    'output_TransactionID': 'N/A',
                    'output_ConversationID': '47bbaba476494860a2c9be30678f4c1c', 'output_ThirdPartyConversationID': 'asv02e5958774f7ba228d83d0d689761'}
        }]

        self.mock_customer2business.return_value.json.return_value = \
            duplicate_transaction_sample

        parameters = {
            'input_Amount': 10,
            'input_Country': 'TZN',
            'input_Currency': 'TZS',
            'input_CustomerMSISDN': '000000000001',
            'input_ServiceProviderCode': '000000',
            'input_ThirdPartyConversationID': 'asv02e5958774f7ba228d83d0d689761',
            'input_TransactionReference': 'T1234C',
            'input_PurchasedItemsDesc': 'Shoes',
        }

        response = self.m_pesa.customer2business(parameters)

        assert self.mock_customer2business.called
        assert response.json() == duplicate_transaction_sample
        assert response.json()[0]['status_code'] == 409
