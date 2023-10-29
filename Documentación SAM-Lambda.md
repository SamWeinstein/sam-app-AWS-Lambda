# Despliegue y Edición de una Función Lambda en AWS SAM con API Gateway

Esta documentación te guiará a través del proceso de despliegue y edición de una función Lambda existente en AWS SAM (Serverless Application Model) y cómo exponerla a través de Amazon API Gateway.

El repositorio de la aplicación SAM junto con el archivo que ejecuta la función Lambda se encuentran en el siguiente repositorio: https://github.com/SamWeinstein/sam-app-AWS-Lambda

## Requisitos Previos
- **Cuenta de AWS:** Asegúrate de tener una cuenta de AWS activa y configurada.
- **AWS CLI:** Instala y configura la AWS Command Line Interface (CLI) en tu sistema local.
- **AWS SAM CLI:** Instala y configura el AWS SAM CLI para trabajar con proyectos de AWS SAM.

## Paso 1: Configuración del Entorno de Desarrollo

Antes de comenzar, asegúrate de tener instalada y configurada la AWS CLI y el AWS SAM CLI en tu sistema local. Si aún no lo has hecho, sigue los pasos de instalación en la [documentación oficial de AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) y la [documentación oficial de AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html).

## Paso 2: Despliegue de la Función Lambda con AWS SAM

Para desplegar tu función Lambda existente con AWS SAM y exponerla a través de API Gateway, sigue estos pasos:

1. Navega a la carpeta raíz de tu proyecto AWS SAM en tu terminal.

2. Utiliza el comando `sam build` para compilar tu aplicación.

3. Utiliza el comando `sam deploy` para desplegar tu función Lambda en AWS Lambda. Este comando te guiará a través del proceso de configuración.

Durante el proceso de configuración, deberás especificar el nombre de la pila CloudFormation y otros parámetros relevantes. Asegúrate de proporcionar la información correcta.

4. Una vez completado el despliegue, recibirás información sobre la ubicación de tu función Lambda y otros recursos relacionados.

## Paso 3: Acceso a través de API Gateway

La función Lambda se expone automáticamente a través de Amazon API Gateway como un endpoint HTTP. Puedes acceder a tu función Lambda a través de la URL proporcionada por API Gateway, que es `https://wx2v9o443h.execute-api.us-east-1.amazonaws.com`.

## Paso 4: Edición de la Función Lambda (Opcional)

Si necesitas editar la lógica de tu función Lambda después del despliegue, sigue estos pasos:

1. Edita el archivo de código fuente de tu función Lambda según tus necesidades. Puedes encontrar el código fuente en la carpeta de tu proyecto AWS SAM.

2. Utiliza el comando `sam build` para compilar la nueva versión de tu función.

3. Utiliza el comando `sam deploy` nuevamente para actualizar tu función Lambda en AWS Lambda.

Durante este proceso, AWS SAM actualizará la función Lambda existente con la nueva versión.

## Conclusión

Este tutorial te ha guiado a través del proceso de desplegar y editar una función Lambda existente utilizando AWS SAM y exponiéndola a través de Amazon API Gateway. Con esta documentación, deberías estar listo para administrar y mantener tus funciones Lambda de manera eficiente. Recuerda seguir las mejores prácticas de seguridad y monitoreo para garantizar un funcionamiento óptimo de tus aplicaciones serverless en AWS Lambda.
