"""Test suite for testing VodaCom M-Pesa reversal transaction
Testing common responses:
- successful transaction: status code 201
- duplicate transaction: status code 409
"""

from unittest.mock import patch

from pypesa.defaults import *
from pypesa.vodacom import MPESA

from .samples import (duplicate_transaction_sample, reversal_parameters,
                      successful_transaction_sample)


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
        self.mock_reversal.return_value.json.return_value = \
            successful_transaction_sample

        response = self.m_pesa.reversal(reversal_parameters)

        assert self.mock_reversal.called
        assert response.json() == successful_transaction_sample
        assert response.json()[0]['status_code'] == 201

    def test_reversal_duplicate_transaction(self):
        """Test for duplicate reversal transaction
        Status code should be 409
        """
        self.mock_reversal.return_value.json.return_value = \
            duplicate_transaction_sample

        response = self.m_pesa.reversal(reversal_parameters)

        assert self.mock_reversal.called
        assert response.json() == duplicate_transaction_sample
        assert response.json()[0]['status_code'] == 409
