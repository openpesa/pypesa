# PyPesa

Python Pesa SDK

## Installation

This package is available in [Python Package Index](https://pypi.org/project/pyppesa/) and can be installed using `pip`:

```
pip install pypesa
```

This package comprises interfaces for interacting with:

- M-PESA/Vodafone vis-a-vis a generic open API that can be used with [Daraja](https://developer.safaricom.co.ke/Documentation); and
- Vodafone vis-a-vis the [Vodacom Open API portal](https://openapiportal.m-pesa.com/login).

To use the generic API interface:

```
from pypesa.open_api import APIContext, APIMethodType, APIRequest
```

To use the `vodacom` module:

```
from pypesa.vodacom import MPESA
```

## Features

- [x] Customer to Business (C2B)
- [x] Business to Customer (B2C)
- [x] Business to Business (B2B)
- [x] Payment Reversal
- [x] Transaction Status
- [x] Direct debit creation and Payment

## Pre-requisites

The following are required and are obtained from [Vodacom Open Api portal](https://openapiportal.m-pesa.com/login):

- API Key
- Public Key

Read more [here](https://pypesa.readthedocs.io/en/latest/).

## Examples

### Customer to Business payment via vodacom m-pesa

```python
# vodacom M-PESA
from pypesa.vodacom import MPESA


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

m_pesa = MPESA(api_key='<your-api-key>',
               public_key='<open-api-public-key>')
response = m_pesa.customer2business(parameters)
```

Check out more examples of methods and responses [here](https://pypesa.readthedocs.io/en/latest/examples/).

## Credits

- [Openpesa](https://github.com/openpesa/)
- [Innocent Zenda](https://github.com/ZendaInnocent)
- [All Contributors](../../contributors)

## License

Code released under [MIT LICENSE](https://github.com/openpesa/pypesa/blob/main/LICENSE)
