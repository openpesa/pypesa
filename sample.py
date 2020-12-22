from pypesa.defaults import MPESA_API_KEY, MPESA_PUBLIC_KEY
from pypesa.vodacom import MPESA

m_pesa = MPESA(MPESA_API_KEY, MPESA_PUBLIC_KEY)
session_id = m_pesa.get_session_id()
print(session_id)

# customer2business
"""
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
response = m_pesa.customer2business(parameters)
print(response)
"""

# reversal of successful transaction
"""
reversal_parameters = {
    'input_ReversalAmount': '25',
    'input_Country': 'TZN',
    'input_ServiceProviderCode': '000000',
    'input_ThirdPartyConversationID':
    'asv02e5958774f7ba228d83d0d689761',
    'input_TransactionID': '0000000000001',
}

response = m_pesa.reversal(reversal_parameters)
print(response)
"""

# business2customer transaction
"""
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

response = m_pesa.business2customer(parameters)
print(response)
"""

# status
'''
parameters = {
    'input_QueryReference': '000000000000000000001',
    'input_ServiceProviderCode': '000000',
    'input_ThirdPartyConversationID': 'asv02e5958774f7ba228d83d0d689761',
    'input_Country': 'TZN',
}

response = m_pesa.status(parameters)
print(response)
'''

# Direct Debit create
''''
parameters = {
    "input_AgreedTC": "1",
    "input_Country": "TZN",
    "input_CustomerMSISDN": "000000000001",
    "input_EndRangeOfDays": "22",
    "input_ExpiryDate": "20211126",
    "input_FirstPaymentDate": "20160324",
    "input_Frequency": "06",
    "input_ServiceProviderCode": "000000",
    "input_StartRangeOfDays": "01",
    "input_ThirdPartyConversationID": "AAA6d1f9391a0052de0b5334a912jbsj1j2kk",
    "input_ThirdPartyReference": "3333"
}

response = m_pesa.direct_debit_create(parameters)
print(response)
'''

# Direct Debit Payment
parameters = {
    "input_Amount": "10",
    "input_Country": "TZN",
    "input_Currency": "TZS",
    "input_CustomerMSISDN": "000000000001",
    "input_ServiceProviderCode": "000000",
    "input_ThirdPartyConversationID": "AAA6d1f939c1005v2de053v4912jbasdj1j2kk",
    "input_ThirdPartyReference": "5db410b459bd433ca8e5"
}

response = m_pesa.direct_debit_payment(parameters)
print(response)
