[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com) [![Build Status](https://travis-ci.org/9cookies/serverless-aws-documentation.svg?branch=master)](https://travis-ci.org/9cookies/serverless-aws-documentation) [![codecov](https://codecov.io/gh/9cookies/serverless-aws-documentation/branch/master/graph/badge.svg)](https://codecov.io/gh/9cookies/serverless-aws-documentation)


### TEST
coverage run --source=cvService -m pytest && coverage report --show-missing

## Install

#### via NPM

Install the serverless CLI via NPM:

```shell
  npm install -g serverless
```

#### Initial setup

Run the command below and follow the prompts:

```shell
  serverless
```

#### Setup with the aws-cli

To set them up through the _aws-cli_ install it first then run aws configure to configure the aws-cli and credentials:

```shell
  aws configure
```

Credentials are stored in INI format in ~_/.aws/credentials_, which you can edit directly if needed.

## Deploy

#### Deployment without stage and region options

```shell
  serverless deploy
```

This is the simplest deployment usage possible. With this command Serverless will deploy your service to the defined
provider in the default stage (dev).

#### Deployment with stage and region options

```shell
    serverless deploy --stage=prod --region=ap-southeast-1
```

With this example we've defined that we want our service to be deployed to the production stage in the region
ap-southeast-1.
