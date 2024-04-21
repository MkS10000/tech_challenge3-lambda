import boto3
import json

def consulta_cpf(cpf):

    dynamodb = boto3.resource('dynamodb')
    tabela = dynamodb.Table('Cliente')

    resposta = tabela.get_item(
        Key={
            'cpf': cpf
        }
    )
    return 'Item' in resposta




def lambda_handler(event, context):
    cpf = event.get('cpf', '')

    if consulta_cpf(cpf):
        return {
            'statusCode': 200,
            'body': ({"token" : "01f8be76-6d32-4cec-9525-e8a4dd1c78f7"})
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('CPF nao esta cadastrado')
        }
