"""Testing VodaCom M-Pesa Direct Debit Payment transaction
Testing common responses:
- successful transaction: status code 201
- duplicate transaction: status code 409
"""

from unittest.mock import patch

from pypesa.defaults import MPESA_API_KEY, MPESA_PUBLIC_KEY
from pypesa.vodacom import MPESA

from .samples import (duplicate_transaction_sample, parameters,
                      successful_transaction_sample)


class TestMpesaBusiness2CustomerTransaction:
    @classmethod
    def setup(cls):
        cls.m_pesa = MPESA(api_key=MPESA_API_KEY, public_key=MPESA_PUBLIC_KEY)
        cls.mock_business2customer_patcher = patch(
            'pypesa.vodacom.MPESA.business2customer')
        cls.mock_business2customer = cls.mock_business2customer_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_business2customer_patcher.stop()

    def test_business2customer_successful_transaction(self):
        """Test for successful business2customer transaction
        Status code should be 201
        """
        self.mock_business2customer.return_value.json.return_value = \
            successful_transaction_sample

        response = self.m_pesa.business2customer(parameters)

        assert self.mock_business2customer.called
        assert response.json() == successful_transaction_sample
        assert response.json()[0]['status_code'] == 201

    def test_business2customer_duplicate_transaction(self):
        """Test for duplicate business2customer transaction
        Status code should be 409
        """
        self.mock_business2customer.return_value.json.return_value = \
            duplicate_transaction_sample

        response = self.m_pesa.business2customer(parameters)

        assert self.mock_business2customer.called
        assert response.json() == duplicate_transaction_sample
        assert response.json()[0]['status_code'] == 409
