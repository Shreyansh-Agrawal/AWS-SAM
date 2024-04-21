# create an s3 bucket
aws s3 mb s3://shreyansh-lambda-sam

# package cfn - upload code to s3
aws cloudformation package --s3-bucket shreyansh-lambda-sam --template-file template.yaml --output-template-file gen/template-generated.yaml
# or sam package ...

# deploy
aws cloudformation deploy --template-file gen/template-generated.yaml --stack-name lambda-sam --capabilities CAPABILITY_IAM
