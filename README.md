# Web backend

Esta es una aplicación serverless que usa el framework [SAM (Serverless Application Model)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) y expone un backend en forma de API.

## Requisitos

Para levantar esta aplicación se debe tener instalado lo siguiente

* Python `3.11.4`
  * Instalar [pyenv](https://github.com/pyenv/pyenv) y luego
  * `pyenv install -v 3.11.4`
  * `pyernv global 3.11.4`
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
* [Docker](https://docs.docker.com/engine/install/)
* [LocalStack](https://docs.localstack.cloud/getting-started/installation/)
  * [LocalStack AWS CLI](https://github.com/localstack/awscli-local)

## Levantar ambiente local

Para levantar el API de manera local se debe ejecutar el siguiente comando

```shell
sam build
````

## Comandos útiles

Invocar función localmente

```shell
sam local invoke HealthCheckFunction --debug --event events/health_check.json
````

Levantar API de forma local

```shell
sam local start-api
````

Se puede probar haciendo un request a [http://localhost:3000/health_check](http://localhost:3000/health_check)

```shell
curl http://localhost:3000/health_check
````

Despliegue

```shell
sam deploy
```

## LocalStack

Levantar emulador local de AWS

```shell
localstack start
```

Efectuar comandos a LocalStack tal como se haría usando AWS CLI, pero con `awslocal`

```shell
awslocal lambda list-functions
```

Desplegar aplicación en LocalStack

```shell
samlocal deploy
```

Ver recursos desplegados en [LocalStack Webapp](https://app.localstack.cloud/)

## Recursos

* [Lambda docs](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
* [SAM docs](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
  * [SAM reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-reference.html)
  * [SAM CLI reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html)
* [SAM Workshop](https://catalog.workshops.aws/complete-aws-sam/en-US)
* [Serverless Patterns Workshop](https://catalog.workshops.aws/serverless-patterns/en-US)
* [Powertools for AWS Lambda](https://docs.powertools.aws.dev/lambda/python/latest/)
* [Serverless Land](https://serverlessland.com/)
