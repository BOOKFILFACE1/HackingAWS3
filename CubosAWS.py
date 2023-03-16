import boto3
from botocore.exceptions import ClientError

# Crea una instancia de cliente para AWS
ec2 = boto3.client('ec2')
s3 = boto3.resource('s3')

# Busca todas las instancias de EC2 y muestra su ID y estado
response = ec2.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print("ID de la instancia:", instance["InstanceId"])
        print("Estado de la instancia:", instance["State"]["Name"])

# Busca todos los buckets de S3 y muestra su nombre y fecha de creación
for bucket in s3.buckets.all():
    print("Nombre del bucket:", bucket.name)
    print("Fecha de creación del bucket:", bucket.creation_date)
    
    # Auditando si el bucket es vulnerable
    try:
        s3.BucketAcl(bucket.name).load()
        s3.BucketPolicy(bucket.name).load()
        print("El bucket {} no es vulnerable".format(bucket.name))
    except ClientError as e:
        if e.response['Error']['Code'] == 'AccessDenied':
            print("El bucket {} es vulnerable".format(bucket.name))
        else:
            print("Error al auditar el bucket {}: {}".format(bucket.name, e))
    
    # Verificando si los archivos del bucket están expuestos al público
    bucket_acl = s3.BucketAcl(bucket.name)
    for grant in bucket_acl.grants:
        grantee = grant['Grantee']
        permission = grant['Permission']
        if 'URI' in grantee and permission == 'READ':
            uri = grantee['URI']
            if uri == 'http://acs.amazonaws.com/groups/global/AllUsers' or uri == 'http://acs.amazonaws.com/groups/global/AuthenticatedUsers':
                print("El archivo {} en el bucket {} está expuesto al público".format(grant['Grantee'], bucket.name))
