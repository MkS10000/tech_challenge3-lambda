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
            'body': json.dumps('CPF está cadastrado')
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('CPF não está cadastrado')
        }    

