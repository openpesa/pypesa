SKIP_REAL = True

"""Sample of parameters and responses."""

# Sample of parameters
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

reversal_parameters = {
    'input_ReversalAmount': '25',
    'input_Country': 'TZN',
    'input_ServiceProviderCode': '000000',
    'input_ThirdPartyConversationID':
    'asv02e5958774f7ba228d83d0d689761',
    'input_TransactionID': '0000000000001',
}

# A sample response for successful transaction
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

# A sample response for duplicate transaction
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

# Direct debit creation
# Successful transaction
successful_debit_creation_response = [{
    'status_code': 201,
    'headers': {
        'date': 'Wed, 16 Dec 2020 07:29:32 GMT',
        'x-frame-options': 'SAMEORIGIN',
        'x-robots-tag': 'none',
        'x-content-type-options': 'nosniff',
        'x-xss-protection': '1; mode=block',
        'strict-transport-security': 'max-age=16005600; includeSubDomains',
        'content-type': 'application/json',
        'access-control-allow-origin': '*',
        'content-length': '258', 'Vary': 'Accept-Encoding'
    },
    'body': {
        'output_ResponseCode': 'INS-0',
        'output_ResponseDesc': 'Request processed successfully',
        'output_TransactionReference': '3333',
        'output_ConversationID': '910b5ff71a6e4d939614cac74ae8c6d9',
        'output_ThirdPartyConversationID': 'AAA6d1f9391a0052de0b5334a912jbsj1j2kk'
    }
}]

duplicate_debit_creation_response = [{
    'status_code': 409,
    'headers': {
        'date': 'Wed, 16 Dec 2020 07:29:32 GMT',
        'x-frame-options': 'SAMEORIGIN',
        'x-robots-tag': 'none',
        'x-content-type-options': 'nosniff',
        'x-xss-protection': '1; mode=block',
        'strict-transport-security': 'max-age=16005600; includeSubDomains',
        'content-type': 'application/json',
        'access-control-allow-origin': '*',
        'content-length': '258', 'Vary': 'Accept-Encoding'
    },
    'body': {
        'output_ResponseCode': 'INS-10',
        'output_ResponseDesc': 'Duplicate Transaction',
        'output_TransactionReference': 'N/A',
        'output_ConversationID': '5d2a711584aa40f1b800cb0db449f46d',
        'output_ThirdPartyConversationID': 'AAA6d1f9391a0052de0b5334a912jbsj1j2kk'
    }
}]


# Direct debit Payment
# Successful transaction
successful_debit_payment_response = [{
    'status_code': 201,
    'headers': {
        'date': 'Wed, 16 Dec 2020 07:29:32 GMT',
        'x-frame-options': 'SAMEORIGIN',
        'x-robots-tag': 'none',
        'x-content-type-options': 'nosniff',
        'x-xss-protection': '1; mode=block',
        'strict-transport-security': 'max-age=16005600; includeSubDomains',
        'content-type': 'application/json',
        'access-control-allow-origin': '*',
        'content-length': '258', 'Vary': 'Accept-Encoding'
    },
    'body': {
        'output_ResponseCode': 'INS-0',
        'output_ResponseDesc': 'Request processed successfully',
        'output_TransactionID': 'mjrDuvWtbfpw',
        'output_ConversationID': '6a7163de90964bfe8a7afeeca974327e',
        'output_ThirdPartyConversationID': 'AAA6d1f939c1005v2de053v4912jbasdj1j2kk'
    }
}]

duplicate_debit_payment_response = [{
    'status_code': 409,
    'headers': {
        'date': 'Wed, 16 Dec 2020 07:29:44 GMT',
        'x-frame-options': 'SAMEORIGIN', 'x-robots-tag': 'none',
        'x-content-type-options': 'nosniff',
        'x-xss-protection': '1; mode=block',
        'strict-transport-security': 'max-age=16005600; includeSubDomains',
        'content-type': 'application/json',
        'access-control-allow-origin': '*',
        'content-length': '241', 'Vary': 'Accept-Encoding'
    },
    'body': {
        'output_ResponseCode': 'INS-10',
        'output_ResponseDesc': 'Duplicate Transaction',
        'output_TransactionID': 'N/A',
        'output_ConversationID': '18336c767c664b6d8a119eb3dada4922',
        'output_ThirdPartyConversationID': 'AAA6d1f939c1005v2de053v4912jbasdj1j2kk'
    }
}]
