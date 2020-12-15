# PyPesa

Python Pesa SDK

## Installation

This package is available in [Python Package Index](https://pypi.org/project/pyppesa/) and can be installed using `pip`

```
pip install pypesa
```

The package comprise both original open API codes and refactored codes.

To use original open API code import `open_api` module

```
from pypesa.open_api import APIContext, APIMethodType, APIRequest
```

To use refactored code import `MPESA` from `vodacom` module.

```
from pypesa.vodacom import MPESA
```

## Features

- [x] Customer to Business (C2B)
- [x] Business to Customer (B2C)
- [x] Business to Business (B2B)
- [x] Payment Reversal
- [x] Transaction Status
- [] Direct debit creation and Payment

## Pre-requisites

The following are required and are obtained from [Vodacom Open Api portal](https://openapiportal.m-pesa.com/login)

- Api Key
- Public Key

See more in [documentation](https://pypesa.readthedocs.io/en/latest/).

## Examples

### Customer to Business payment via vodacom m-pesa

```python
# vodacom M-PESA
from mobile_payments.vodacom import MPESA

api_key = '<your-api-key>'
public_key = '<open-api-public-key>'

m_pesa = MPESA(api_key=api_key, public_key=public_key)

# Customer to Business payment
parameters = {
    'input_Amount': '1000', # amount to be charged
    'input_Country': 'TZN',
    'input_Currency': 'TZS',
    'input_CustomerMSISDN': '000000000001',
    'input_ServiceProviderCode': '000000',
    'input_ThirdPartyConversationID': 'c9e794e10c63479992a8b08703abeea36',
    'input_TransactionReference': 'T23434ZE3',
    'input_PurchasedItemsDesc': 'Shoes',
}

response = m_pesa.customer2business(parameters)
```

Check more examples of methods and responses in [docs](https://pypesa.readthedocs.io/en/latest/examples/)

## License

Code released under [MIT LICENSE](https://github.com/openpesa/pypesa/blob/main/LICENSE)
