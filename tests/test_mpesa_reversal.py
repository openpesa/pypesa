"""Test suite for testing VodaCom M-Pesa reversal transaction
Testing common responses:
- successful transaction: status code 201
- duplicate transaction: status code 409
"""

from unittest.mock import patch

from pypesa.defaults import *
from pypesa.vodacom import MPESA


class TestMpesaReversalTransaction:
    @classmethod
    def setup(cls):
        cls.m_pesa = MPESA(api_key=MPESA_API_KEY, public_key=MPESA_PUBLIC_KEY)
        cls.mock_reversal_patcher = patch(
            'pypesa.vodacom.MPESA.reversal')
        cls.mock_reversal = cls.mock_reversal_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_reversal_patcher.stop()

    def test_reversal_successful_transaction(self):
        """Test for successful reversal transaction
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

        self.mock_reversal.return_value.json.return_value = \
            successful_transaction_sample

        reversal_parameters = {
            'input_ReversalAmount': '25',
            'input_Country': 'TZN',
            'input_ServiceProviderCode': '000000',
            'input_ThirdPartyConversationID':
            'asv02e5958774f7ba228d83d0d689761',
            'input_TransactionID': '0000000000001',
        }

        response = self.m_pesa.reversal(reversal_parameters)

        assert self.mock_reversal.called
        assert response.json() == successful_transaction_sample
        assert response.json()[0]['status_code'] == 201

    def test_reversal_duplicate_transaction(self):
        """Test for duplicate reversal transaction
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

        self.mock_reversal.return_value.json.return_value = \
            duplicate_transaction_sample

        reversal_parameters = {
            'input_ReversalAmount': '25',
            'input_Country': 'TZN',
            'input_ServiceProviderCode': '000000',
            'input_ThirdPartyConversationID':
            'asv02e5958774f7ba228d83d0d689761',
            'input_TransactionID': '0000000000001',
        }

        response = self.m_pesa.reversal(reversal_parameters)

        assert self.mock_reversal.called
        assert response.json() == duplicate_transaction_sample
        assert response.json()[0]['status_code'] == 409
