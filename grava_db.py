def lambda_handler(event, context):
    print("Arquivo processado com sucesso!")

    return {
        'statusCode': 200,
        'body': 'Processamento concluído'
    }