# HackingAWS3
👋 ¡Hola, comunidad de BOOKFILFACE! Hoy quiero presentarles un script en Python que he creado para buscar servidores y auditar buckets de S3.

🔍 Este script utiliza la biblioteca boto3 para buscar todas las instancias de EC2 y todos los buckets de S3 en su cuenta de AWS.

🛡️ Luego, el script audita cada bucket de S3 para verificar si es vulnerable. Utiliza el método load() de las clases BucketAcl y BucketPolicy de boto3 para verificar si existen políticas o permisos públicos en el bucket. Si no hay políticas ni permisos públicos, el script indica que el bucket no es vulnerable. Si existe una política o permiso público, el script indica que el bucket es vulnerable.

👀 Además, el script también verifica si los archivos del bucket están expuestos al público. Para hacer esto, utiliza el objeto BucketAcl para obtener la lista de permisos para el bucket y luego verifica si hay algún permiso con el valor READ para un usuario público o para usuarios autenticados. Si se encuentra un permiso de lectura público, el script indica que el archivo está expuesto.

👨‍💻 Este script es una herramienta útil para los propietarios de cuentas de AWS que desean auditar sus buckets de S3 para detectar vulnerabilidades y asegurarse de que los archivos no estén expuestos al público.

🙌 Espero que este script sea de utilidad para su trabajo en AWS. Si tiene alguna pregunta o sugerencia, no dude en contactarme. ¡Gracias por su atención! 🚀
