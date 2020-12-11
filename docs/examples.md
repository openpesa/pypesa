# Getting Started

To be able to make any transaction via open api portal, it is required to have an API key that exchanged for a session key. A valid session key is needed for every transaction.

API key is created whenever app is created.

The platform also provides public key for sandbox and open api.
Sandbox is used for testing, when it is ready to make live open api is used.

The procedure are the same for testing and live though different public key are used for each environment. Since this focus more on testing for now, the public key to be used is sandbox public key.

```
public_key = 'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEArv9yxA69XQKBo24BaF/D+fvlqmGdYjqLQ5WtNBb5tquqGvAvG3WMFETVUSow/LizQalxj2ElMVrUmzu5mGGkxK08bWEXF7a1DEvtVJs6nppIlFJc2SnrU14AOrIrB28ogm58JjAl5BOQawOXD5dfSk7MaAA82pVHoIqEu0FxA8BOKU+RGTihRU+ptw1j4bsAJYiPbSX6i71gfPvwHPYamM0bfI4CmlsUUR3KvCG24rB6FNPcRBhM3jDuv8ae2kC33w9hEq8qNB55uw51vK7hyXoAa+U7IqP1y6nBdlN25gkxEA8yrsl1678cspeXr+3ciRyqoRgj9RD/ONbJhhxFvt1cLBh+qwK2eqISfBb06eRnNeC71oBokDm3zyCnkOtMDGl7IvnMfZfEPFCfg5QgJVk1msPpRvQxmEsrX9MQRyFVzgy2CWNIb7c+jPapyrNwoUbANlN8adU1m6yOuoX7F49x+OjiG2se0EJ6nafeKUXw/+hiJZvELUYgzKUtMAZVTNZfT8jjb58j8GVtuS+6TM2AutbejaCV84ZK58E2CRJqhmjQibEUO6KPdD7oTlEkFy52Y1uOOBXgYpqMzufNPmfdqqqSM4dU70PO8ogyKGiLAIxCetMjjm6FCMEA3Kc8K0Ig7/XtFm9By6VxTJK1Mg36TlHaZKP6VzVLXMtesJECAwEAAQ=='
```

## Examples

### Customer to business transaction

```python
from pyepsa.vodacom import MPESA

m_pesa = MPESA(api_key=<api-key>, public_key=<platform-public-key>)

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

results = m_pesa.customer2business(parameters)
```

### Business to customer transaction

```python
from pypesa.vodacom import MPESA

m_pesa = MPESA(api_key=<api-key>, public_key=<platform-public-key>)

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

results = m_pesa.business2customer(parameters)
```

### Business to business transaction

```python
from pypesa.vodacom import MPESA

m_pesa = MPESA(api_key=<api-key>, public_key=<platform-public-key>)

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

results = m_pesa.business2business(parameters)
```

### Reversal transaction

```python
from pypesa.vodacom import MPESA

m_pesa = MPESA(api_key=<api-key>, public_key=<platform-public-key>)

reversal_parameters = {
    'input_ReversalAmount': '25',
    'input_Country': 'TZN',
    'input_ServiceProviderCode': '000000',
    'input_ThirdPartyConversationID': 'asv02e5958774f7ba228d83d0d689761',
    'input_TransactionID': '0000000000001',
}

results = m_pesa.reversal(reversal_parameters)
```

### Query transaction status

```python
from pypesa.vodacom import MPESA

m_pesa = MPESA(api_key=<api-key>, public_key=<platform-public-key>)

parameters = {
    'input_QueryReference': '000000000000000000001',
    'input_ServiceProviderCode': '000000',
    'input_ThirdPartyConversationID':'asv02e5958774f7ba228d83d0d689761',
    'input_Country': 'TZN',
}

results = m_pesa.status(parameters)
```

## Sample Responses

### Successful Transaction

```
[{
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
```

### Duplicate Transaction

```
[{
    'status_code': 409,
    'headers': {'date': 'Sun, 06 Dec 2020 05:12:04 GMT',
                        'x-frame-options': 'SAMEORIGIN', 'x-robots-tag': 'none', 'x-content-type-options': 'nosniff',
                        'x-xss-protection': '1; mode=block', 'strict-transport-security': 'max-age=16005600; includeSubDomains',
                        'content-type': 'application/json',
                        'access-control-allow-origin': '*', 'content-length': '235', 'Vary': 'Accept-Encoding'},
    'body': {'output_ResponseCode': 'INS-10',
             'output_ResponseDesc': 'Duplicate Transaction',
             'output_TransactionID': 'N/A',
             'output_ConversationID': '47bbaba476494860a2c9be30678f4c1c',
             'output_ThirdPartyConversationID': 'asv02e5958774f7ba228d83d0d689761'}
}]
```
