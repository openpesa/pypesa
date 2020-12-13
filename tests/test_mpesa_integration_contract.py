from unittest import skipIf
from unittest.mock import patch

from pypesa.defaults import MPESA_API_KEY, MPESA_PUBLIC_KEY
from pypesa.vodacom import MPESA

from .samples import SKIP_REAL, parameters, successful_transaction_sample


class TestIntegrationContract:
    """Testing for updates to the API data.
        - Call the service to hit the mocked API.
        - Call the service to hit the actual API.
        - An object from the actual API and an object from the mocked API
        should have the same data structure.
    """
    @classmethod
    def setup(cls):
        cls.m_pesa = MPESA(api_key=MPESA_API_KEY, public_key=MPESA_PUBLIC_KEY)

    @skipIf(SKIP_REAL, 'Skipping tests that hit the real API server.')
    def test_successful_transaction(self):
        # Call the service to hit the mocked API.
        m_pesa = MPESA(api_key=MPESA_API_KEY, public_key=MPESA_PUBLIC_KEY)
        actual_response = m_pesa.customer2business(parameters)
        actual_keys = actual_response.json().pop().keys()

        # Call the service to hit the mocked API.
        with patch(
                'pypesa.vodacom.MPESA.customer2business'
        ) as mock_customer2business:
            mock_customer2business.return_value.json.return_value = \
                successful_transaction_sample

            mocked_response = self.m_pesa.customer2business(parameters)

            assert mock_customer2business.called
            mocked_keys = mocked_response.json().pop().keys()

        # compare data structure of actual and mocked keys
        assert list(actual_keys) == list(mocked_keys)
