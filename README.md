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


There are two primary lambdas that do the heavy lifting. The first is "hostIsUp" - this is tied to a PUT endpoint on API Gateway. The second is "checkIfHostIsUp" - this is invoked from EventBridge on a schedule. Both Lambdas query DynamoDB for their functionality. SNS is used

### Walkthrough