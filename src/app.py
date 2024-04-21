print('loading function')

def lambda_handler(event, context):
    print('Event:\n', event)
    print('Context:\n', context)

    return 'Hello SAM'
