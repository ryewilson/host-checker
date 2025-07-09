# Host Checker

## Introduction

This repo contains scripts and AWS Lambdas that work together to test whether a given server has internet access. Specifically, these are used to detect when an internet connection is down for more than a few minutes.

## How it works

### Services used

The primary services used are:

- AWS API Gateway
- AWS Lambda
- AWS DynamoDB
- AWS Eventbridge
- AWS SNS


There are two primary lambdas that do the heavy lifting. The first is "hostIsUp" - this is tied to a PUT endpoint on API Gateway. The second is "checkIfHostIsUp" - this is invoked from EventBridge on a schedule. Both Lambdas query DynamoDB for their functionality. SNS is used to notify when a host changes state.

### Walkthrough

TODO: add step-by-step how it functions

## How to use it

In order to use the code in this repo you need:

- An AWS account (free tier is fine)
- [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) installed
- Python 3.13 installed


## How to re-deploy

TODO: Describe how to re-build and deploy the changes to a lambda