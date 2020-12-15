# Integration in Projects

## Django

```python
# views.py

from django.conf import settings
from django.contrib import messages
from django.utils.crypto import get_random_string

from pypesa.vodacom import MPESA

def payment(request):
    temlate_name = ''
    context = {'form': PaymentForm()}


    if request.method == 'POST':
            form = PaymentForm(request.POST)
            if form.is_valid():
                # Instatiate API context
                m_pesa = MPESA(api_key, public_key)

            # Constructing parameters
                parameters = {
                    'input_Amount': 10,
                    'input_Country': 'TZN',
                    'input_Currency': 'TZS',
                    'input_CustomerMSISDN': request.POST.get('phone'),
                    'input_ServiceProviderCode': '000000',
                    'input_ThirdPartyConversationID': get_random_string(18),
                    'input_TransactionReference': get_random_string(18),
                    'input_PurchasedItemsDesc': 'Shoes',
                }

                # make an API call
                results = m_pesa.c2b(parameters)

                # processing results from API call
                if results.body['output_ResponseCode'] == 'INS-0':
                    # add your logic here
                    # example: saving results to the database.

                    messages.success(
                        request, 'Your Payment was Successfully sent!')

                else:
                    messages.error(request, results.body['output_ResponseDesc'])

        return render(request, template_name, context)
```

### Environmental variables

Create `.env` file in the root of the project if not exists. Fill in the API key.

```
# .env

MPESA_API_KEY = ''

MPESA_PUBLIC_KEY=MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEArv9yxA69XQKBo24BaF/D+fvlqmGdYjqLQ5WtNBb5tquqGvAvG3WMFETVUSow/LizQalxj2ElMVrUmzu5mGGkxK08bWEXF7a1DEvtVJs6nppIlFJc2SnrU14AOrIrB28ogm58JjAl5BOQawOXD5dfSk7MaAA82pVHoIqEu0FxA8BOKU+RGTihRU+ptw1j4bsAJYiPbSX6i71gfPvwHPYamM0bfI4CmlsUUR3KvCG24rB6FNPcRBhM3jDuv8ae2kC33w9hEq8qNB55uw51vK7hyXoAa+U7IqP1y6nBdlN25gkxEA8yrsl1678cspeXr+3ciRyqoRgj9RD/ONbJhhxFvt1cLBh+qwK2eqISfBb06eRnNeC71oBokDm3zyCnkOtMDGl7IvnMfZfEPFCfg5QgJVk1msPpRvQxmEsrX9MQRyFVzgy2CWNIb7c+jPapyrNwoUbANlN8adU1m6yOuoX7F49x+OjiG2se0EJ6nafeKUXw/+hiJZvELUYgzKUtMAZVTNZfT8jjb58j8GVtuS+6TM2AutbejaCV84ZK58E2CRJqhmjQibEUO6KPdD7oTlEkFy52Y1uOOBXgYpqMzufNPmfdqqqSM4dU70PO8ogyKGiLAIxCetMjjm6FCMEA3Kc8K0Ig7/XtFm9By6VxTJK1Mg36TlHaZKP6VzVLXMtesJECAwEAAQ==
```

!!!note
    It is recommended to store confidental information for services in environmental variables.

Load enviromental variables using a package of your choice.

This guide uses `django-decouple` and can be installed using `pip`

```
pip install django-decouple
```

To be able to use `.env` variables, you have to load them in `settings.py`.

```python
# settings.py

from decouple import config

MPESA_API_KEY = config('MPESA_API_KEY')
MPESA_PUBLIC_KEY = config('MPESA_PUBLIC_KEY')
```

The package has default values for endpoints. All default values are for development purposes only.

All defaults values used are listed [here](../vodacom/#default-values)

!!!note
    Remember to override the defaults in production to corresponding endpoints.

To be able to access `settings` in `views`, make sure to import them.

```python
from django.conf import settings

api_key = settings.MPESA_API_KEY
public_key = settings.MPESA_PUBLIC_KEY
```

### Instatiate API Context

```python
m_pesa = MPESA(api_key, public_key)
```

### Constucting transaction parameters

Each transaction method requires parameters which is dictionary. Example of parameters for `customer2business` transaction:

```
parameters = {
    'input_Amount': '10',
    'input_Country': 'TZN',
    'input_Currency': 'TZS',
    'input_CustomerMSISDN': '000000000001',
    'input_ServiceProviderCode': '000000',
    'input_ThirdPartyConversationID':
    'asv02e5958774f7ba228d83d0d689761',
    'input_TransactionReference': 'T1234C',
    'input_PaymentItemsDesc': 'Salary payment',
}
```

There are number of items needed for successful transaction. Some are default for now and are sane. If you need different values, check the [open api documentation](https://openapiportal.m-pesa.com/api-documentation) for more information.

For this guide, we focus on how to get values for:

- `input_Amount`

    Amount to be charged. It can be obtained from the price of the product or service.

- `input_CustomerMSISDN`

    This is the phone number of the customer to be charged. In your `form`, remember to include the `phone` field to be able to get the number using `request.POST.get('phone')`. Length required is between 12 and 14 inclusive.

    !!!note
        `000000000001` is the number provided for testing purposes only. Use it in development.

- `input_ServiceProviderCode`

    The shortcode of the organization where funds will be creditted to. It is required and can have 5 to 10 digits.

- `input_ThirdPartyConversationID`

    The third party's transaction reference on their system. It is required and can have a characters of length between 1 and 40 inclusive.

- `input_TransactionReference`

    The customer's transaction reference. It is required and can have characters of length between 1 and 20 inclusive.

- `input_PaymentItemsDesc`

    Description of the purchased item. It is required and can have characters of length between 1 and 256 inclusive.

### Make an API call

Make API call for method.

General format:

```python
results = m_pesa.method(parameters)
```

Examples:

```python
# cutomer-to-business
results = m_pesa.customer2business(parameters)

# business-to-customer
results = m_pesa.business2customer(parameters)

# business-to-business
results = m_pesa.business2business(parameters)
```

### Processing the results from API call

The results of API call can be processed by checking the response code. More information check on [response codes](https://openapiportal.m-pesa.com/api-documentation#ResponseCodes).

Check response code by comparing `results.body[output_ResponseCode]` with known response codes. [Sample responses](../examples/#sample-responses)

Each code has its own unique message. Instead of checking against each reponse status, we just test for `INS-0` for successful transaction and all other codes are considered as error. Message for each code can be accessed using `results.body[output_ResponseDesc]`.
