# Vodacom M-Pesa

The `vodacom` module provides one key class: `MPESA` responsible for all M-Pesa transactions.

Use it by defining instance along with arguments required. Here is an example:

```python
from mobile_payments.vodacom import MPESA


m_pesa = MPESA(api_key=<api-key>, public_key=<platform-public-key>)
```

Configure `context` that's necessary for every method available.

Args:

- `api_key [string]`

    Application API key. The portal provides it in application section on dashboard when application is created. It is needed to authorise and authenticate your application on the server.

    !!!note
        This is required, if not provided in the `MPESA` class instance, there is no default value set.

- `public_key [string]`

    Open API platform public key. The key used to encrypt application API key.

```
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEArv9yxA69XQKBo24BaF/D+fvlqmGdYjqLQ5WtNBb5tquqGvAvG3WMFETVUSow/LizQalxj2ElMVrUmzu5mGGkxK08bWEXF7a1DEvtVJs6nppIlFJc2SnrU14AOrIrB28ogm58JjAl5BOQawOXD5dfSk7MaAA82pVHoIqEu0FxA8BOKU+RGTihRU+ptw1j4bsAJYiPbSX6i71gfPvwHPYamM0bfI4CmlsUUR3KvCG24rB6FNPcRBhM3jDuv8ae2kC33w9hEq8qNB55uw51vK7hyXoAa+U7IqP1y6nBdlN25gkxEA8yrsl1678cspeXr+3ciRyqoRgj9RD/ONbJhhxFvt1cLBh+qwK2eqISfBb06eRnNeC71oBokDm3zyCnkOtMDGl7IvnMfZfEPFCfg5QgJVk1msPpRvQxmEsrX9MQRyFVzgy2CWNIb7c+jPapyrNwoUbANlN8adU1m6yOuoX7F49x+OjiG2se0EJ6nafeKUXw/+hiJZvELUYgzKUtMAZVTNZfT8jjb58j8GVtuS+6TM2AutbejaCV84ZK58E2CRJqhmjQibEUO6KPdD7oTlEkFy52Y1uOOBXgYpqMzufNPmfdqqqSM4dU70PO8ogyKGiLAIxCetMjjm6FCMEA3Kc8K0Ig7/XtFm9By6VxTJK1Mg36TlHaZKP6VzVLXMtesJECAwEAAQ ==
```

Optional Args:

- `ssl [boolean]`

    Controls whether to use `http` or `https`. You typically want this enabled. Defaults to `True`.

## Methods

### `get_encrypted_api_key()`

A method used to generated encrypted API key. Does not require any arguments.
Returns encrypted API key.

### `get_session_id()`

A method to generate valid Session ID needed to transact on M-Pesa using OpenAPI. When successful, returns a valid session key.

Args:

- `path [string]`

    A URL for creating a session.

    Format: `/[environment]/ipg/v2/[market]/getSession/`

    Defaults to `/sandbox/ipg/v2/vodacomTZN/getSession/`.

!!!note
    The methods above are used internally and you don't have to use them directly unless needed.

### `customer2business()`

A method for customer-to-business transaction.

Args:

- `parameters [dict]`

    A key-pair values that contains all necessary parameters for successful customer-to-business transaction.

    Example of `parameters`:

```python
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
```

- `path [string]`

    A URL for customer-to-business transaction.

    Format: `/[environment]/ipg/v2/[market]/c2bPayment/singleStage/`

    Defaults to `/sandbox/ipg/v2/vodacomTZN/c2bPayment/singleStage/`

### `reversal()`

A method for reversing a successful transaction.

Args:

- `reversal_parameters [dict]`

    A key-pair values that contains all necessary parameters for successful reversal of a transaction.

    Example of `reversal_parameters`:

```python
reversal_parameters = {
    'input_ReversalAmount': '25',
    'input_Country': 'TZN',
    'input_ServiceProviderCode': '000000',
    'input_ThirdPartyConversationID': 'asv02e5958774f7ba228d83d0d689761',
    'input_TransactionID': '0000000000001',
}
```

- `path [string]`

    A URL for reversing a successful transaction.

    Format: `/[environment]/ipg/v2/[market]/reversal/`

    Defaults to `/sandbox/ipg/v2/vodacomTZN/reversal/`

### `business2customer()`

A method for standard business-to-customer transaction.

Args:

- `parameters [dict]`

    A key-pair values that contains all necessary parameters for successful business-to-customer transaction.

    Example of `parameters`:

```python
parameters = {
    'input_Amount': '10',
    'input_Country': 'TZN',
    'input_Currency': 'TZS',
    'input_CustomerMSISDN': '000000000001',
    'input_ServiceProviderCode': '000000',
    'input_ThirdPartyConversationID': 'asv02e5958774f7ba228d83d0d689761',
    'input_TransactionReference': 'T1234C',
    'input_PaymentItemsDesc': 'Salary payment',
}
```

- `path [string]`

    A URL for business-to-customer transaction.

    Format: `/[environment]/ipg/v2/[market]/b2cPayment/`

    Defaults to `/sandbox/ipg/v2/vodacomTZN/b2cPayment/`

### `business2business()`

A method for standard business-to-business transaction.

Args:

- `parameters [dict]`

    A key-pair values that contains all necessary parameters for successful business-to-business transaction.

    Example of `parameters`:

```python
parameters = {
    'input_Amount': '10',
    'input_Country': 'TZN',
    'input_Currency': 'TZS',
    'input_CustomerMSISDN': '000000000001',
    'input_ServiceProviderCode': '000000',
    'input_ThirdPartyConversationID': 'asv02e5958774f7ba228d83d0d689761',
    'input_TransactionReference': 'T1234C',
    'input_PaymentItemsDesc': 'Salary payment',
}
```

- `path [string]`

    A URL for business-to-business transaction.

    Format: `/[environment]/ipg/v2/[market]/b2bPayment/`

    Defaults to `/sandbox/ipg/v2/vodacomTZN/b2bPayment/`

### `status()`

A method for querying the status of the transaction that has been initiated.

Args:

- `parameters [dict]`

    A key-pair values that contains all necessary parameters for querying the status of initiated transaction.

    Example of `parameters`:

```python
parameters = {
    'input_QueryReference': '000000000000000000001',
    'input_ServiceProviderCode': '000000',
    'input_ThirdPartyConversationID': 'asv02e5958774f7ba228d83d0d689761',
    'input_Country': 'TZN',
}
```

- `path [string]`

    A URL for business-to-business transaction.

    Format: `/[environment]/ipg/v2/[market]/queryTransactionStatus/`

    Defaults to `/sandbox/ipg/v2/vodacomTZN/queryTransactionStatus/`

## Default values

Default values used for development.

```
MPESA_BASE_URL = 'openapi.m-pesa.com'
MPESA_GET_SESSION_URL = '/sandbox/ipg/v2/vodacomTZN/getSession/'
MPESA_C2BPAYMENT_URL = '/sandbox/ipg/v2/vodacomTZN/c2bPayment/singleStage/'
MPESA_REVERSAL_URL = '/sandbox/ipg/v2/vodacomTZN/reversal/'
MPESA_B2CPAYMENT_URL = '/sandbox/ipg/v2/vodacomTZN/b2cPayment/'
MPESA_B2BPAYMENT_URL = '/openapi/ipg/v2/vodacomTZN/b2bPayment/'
MPESA_TRANSACTION_STATUS_URL = '/openapi/ipg/v2/vodacomTZN/queryTransactionStatus/'
```

- [environment] - sandobox
- [market] - vodacomTZN
