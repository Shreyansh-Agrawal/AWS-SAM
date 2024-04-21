import json

print('loading function')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    print('Event:\n' + json.dumps(event, indent=2))
    print('Context:\n', context)

    return respond(None, res='Hellow SAM from Lambda')
